async function loadData() {

    const response = await fetch("/api/linux");
    const data = await response.json();

    document.getElementById("hostname").textContent = data.hostname;
    document.getElementById("cpu").textContent = data.cpu_usage + "%";
    document.getElementById("memory").textContent = data.memory_usage + "%";
    document.getElementById("disk").textContent = data.disk_usage + "%";
    document.getElementById("uptime").textContent = data.uptime;
    document.getElementById("time").textContent = data.current_time;
    document.getElementById("health").textContent = data.health;
}

loadData();

setInterval(loadData,5000);
