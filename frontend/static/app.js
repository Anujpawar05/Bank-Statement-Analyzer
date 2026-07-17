document
.getElementById("upload-form")
.addEventListener("submit", async function(e){

e.preventDefault();

const file =
document.getElementById("file").files[0];

if(!file)return;

const formData = new FormData();

formData.append("file",file);

document.getElementById("status").innerText =
"Analyzing...";

const response = await fetch("/analyze",{

method:"POST",

body:formData

});

const blob =
await response.blob();

const url =
window.URL.createObjectURL(blob);

const a =
document.createElement("a");

a.href=url;

a.download="analysis.xlsx";

a.click();

document.getElementById("status").innerText =
"Done.";

});