const canvas = document.getElementById("pad");
const ctx = canvas.getContext("2d");

let drawing = false;

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => {
    drawing = false;
    ctx.beginPath();
});
canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!drawing) return;

    ctx.lineWidth = 15;
    ctx.lineCap = "round";
    ctx.strokeStyle = "black";

    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
}

document.getElementById("clear").onclick = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

document.getElementById("classify").onclick = async () => {
    const dataURL = canvas.toDataURL("image/png");

    const res = await fetch("/api/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ image: dataURL })
    });

    const result = await res.json();

    document.getElementById("result").innerText =
        `Prediction: ${result.digit} (${result.confidence})`;

    loadHistory();
};

async function loadHistory() {
    const res = await fetch("/api/history");
    const data = await res.json();

    const list = document.getElementById("history");
    list.innerHTML = "";

    data.forEach(item => {
        const li = document.createElement("li");
        li.innerText = `${item[0]} → ${item[1]} (${item[2]})`;
        list.appendChild(li);
    });
}

loadHistory();
