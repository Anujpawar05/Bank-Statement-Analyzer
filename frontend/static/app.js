const fileInput = document.getElementById("pdfFile");
const dropArea = document.getElementById("dropArea");
const filename = document.getElementById("filename");
const button = document.getElementById("analyzeBtn");
const status = document.getElementById("status");
const spinner = document.getElementById("spinner");

const progressBar = document.getElementById("progressBar");
const progressStep = document.getElementById("progressStep");
const progressTimer = document.getElementById("progressTimer");

const results = document.getElementById("results");

const bankName = document.getElementById("bankName");
const holderName = document.getElementById("holderName");
const statementPeriod = document.getElementById("statementPeriod");

const income = document.getElementById("income");
const expense = document.getElementById("expense");
const cashFlow = document.getElementById("cashFlow");
const transactionCount = document.getElementById("transactionCount");
const downloadBtn = document.getElementById("downloadBtn");
const resetBtn = document.getElementById("resetBtn");
const passwordContainer = document.getElementById("passwordContainer");
const passwordInput = document.getElementById("pdfPassword");

console.log("app.js loaded with progress & nature classification");
let selectedFile = null;
let progressInterval = null;
let timerInterval = null;
let startTime = 0;

/* ---------------------------------------
   File Selection
--------------------------------------- */

fileInput.addEventListener("change", () => {
    if (!fileInput.files.length) return;
    selectedFile = fileInput.files[0];
    filename.textContent = selectedFile.name;
    button.disabled = false;
    status.innerHTML = "";
});

/* ---------------------------------------
   Drag & Drop
--------------------------------------- */

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.style.background = "#eef6ff";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.background = "";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.style.background = "";
    if (!e.dataTransfer.files.length) return;
    selectedFile = e.dataTransfer.files[0];
    fileInput.files = e.dataTransfer.files;
    filename.textContent = selectedFile.name;
    button.disabled = false;
    status.innerHTML = "";
});

/* ---------------------------------------
   Progress Tracker Helper
--------------------------------------- */

function startProgressTracker() {
    spinner.hidden = false;
    startTime = Date.now();
    let currentPercent = 10;
    if (progressBar) progressBar.style.width = "10%";
    if (progressStep) progressStep.textContent = "1/4: Uploading PDF statement...";

    timerInterval = setInterval(() => {
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        if (progressTimer) progressTimer.textContent = `Elapsed: ${elapsed}s`;
    }, 1000);

    const stages = [
        { afterMs: 2500, percent: 35, text: "2/4: Scanning & performing OCR extraction..." },
        { afterMs: 12000, percent: 65, text: "2/4: Processing statement pages with OCR..." },
        { afterMs: 22000, percent: 80, text: "3/4: Parsing transactions & verifying debit/credit balance..." },
        { afterMs: 32000, percent: 92, text: "4/4: Reconciling values & generating Excel workbook..." },
    ];

    stages.forEach(stage => {
        setTimeout(() => {
            if (startTime > 0) {
                if (progressBar) progressBar.style.width = stage.percent + "%";
                if (progressStep) progressStep.textContent = stage.text;
            }
        }, stage.afterMs);
    });
}

function stopProgressTracker() {
    startTime = 0;
    if (timerInterval) clearInterval(timerInterval);
    if (progressBar) progressBar.style.width = "100%";
    if (progressStep) progressStep.textContent = "Complete!";
}

/* ---------------------------------------
   Upload & Analyze
--------------------------------------- */

button.addEventListener("click", async (e) => {
    e.preventDefault();
    if (!selectedFile && fileInput.files.length) {
        selectedFile = fileInput.files[0];
    }
    if (!selectedFile) {
        status.innerHTML = `<span style="color:#dc2626;">⚠️ Please select or drop a bank statement PDF first.</span>`;
        return;
    }

    button.disabled = true;
    status.innerHTML = "";
    results.hidden = true;

    startProgressTracker();

    const formData = new FormData();
    formData.append("file", selectedFile);
    if (passwordInput.value.trim() !== "") {
        formData.append("password", passwordInput.value.trim());
    }

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            let errorText = "Server Error";
            try {
                const errJson = await response.json();
                errorText = errJson.detail || errJson.message || "Server Error";
            } catch (_) {}
            throw new Error(errorText);
        }

        const data = await response.json();
        stopProgressTracker();

        if (data.requires_password) {
            spinner.hidden = true;
            status.innerHTML = `<span style="color:#d97706;">⚠️ ${data.message}</span>`;
            passwordContainer.hidden = false;
            button.disabled = false;
            passwordInput.focus();
            return;
        }

        if (data.error) {
            spinner.hidden = true;
            status.innerHTML = `<span style="color:#dc2626;">⚠️ ${data.message}</span>`;
            button.disabled = false;
            return;
        }

        spinner.hidden = true;
        status.innerHTML = "Analysis Complete ✔";

        /* ----------------------------
           Metadata
        ---------------------------- */
        bankName.textContent = data.metadata.bank_name || "-";
        holderName.textContent = data.metadata.account_holder || "-";
        statementPeriod.textContent = data.metadata.statement_period || "-";

        /* ----------------------------
           Financial Summary
        ---------------------------- */
        const formatCurrency = (amount) =>
            "₹ " + Number(amount).toLocaleString("en-IN", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

        income.textContent = formatCurrency(data.analysis.total_credit ?? 0);
        expense.textContent = formatCurrency(data.analysis.total_debit ?? 0);
        cashFlow.textContent = formatCurrency(data.analysis.net_cash_flow ?? 0);
        transactionCount.textContent = data.transaction_count ?? 0;

        /* ----------------------------
           Download Button
        ---------------------------- */
        downloadBtn.href = data.download_url;

        /* ----------------------------
           Show Dashboard
        ---------------------------- */
        document.querySelector(".container").style.display = "none";
        results.hidden = false;

        /* ----------------------------
           Reset Form Inputs
        ---------------------------- */
        fileInput.value = "";
        selectedFile = null;
        passwordInput.value = "";
        filename.textContent = "No file selected";
        button.disabled = true;

    } catch (error) {
        console.error(error);
        stopProgressTracker();
        spinner.hidden = true;
        status.innerHTML = `<span style="color:#dc2626;">❌ ${error.message || "Something went wrong during processing. Please try again."}</span>`;
        button.disabled = false;
    }
});

if (passwordInput) {
    passwordInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            button.click();
        }
    });
}

if (resetBtn) {
    resetBtn.addEventListener("click", () => {
        results.hidden = true;
        document.querySelector(".container").style.display = "flex";
        status.innerHTML = "";
    });
}