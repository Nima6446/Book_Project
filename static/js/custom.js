// فراخوانی API از اپ هوم
fetch("/api/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("site-title").innerText = data.site_name;
    })
    .catch(error => console.error("خطا در دریافت API:", error))

