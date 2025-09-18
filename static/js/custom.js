
//site header
(async function loadSiteSettings() {
  try {
    // مسیر API رو مطابق urls خودت بذار
    const res = await fetch("/api/v1/settings/");
    const data = await res.json();

    if (!data.settings) return;
    const settings = data.settings;

    // لوگو
    const $logo = document.getElementById("site-logo");
    if ($logo && settings.site_logo) {
      $logo.src = settings.site_logo;
      $logo.alt = settings.site_name || "Site Logo";
    }

    // تلفن
    const $tell = document.getElementById("site-tell");
    if ($tell && settings.tell) {
      const tel = settings.tell.trim();
      $tell.textContent = tel;
      $tell.href = "tel:" + tel.replace(/\s+/g, "");
    }

    // ایمیل
    const $email = document.getElementById("site-email");
    if ($email && settings.email) {
      const mail = settings.email.trim();
      $email.textContent = mail;
      $email.href = "mailto:" + mail;
    }

    // آدرس (مثلاً برای فوتر)
    const $address = document.getElementById("site-address");
    if ($address && settings.addres) {
      $address.textContent = settings.addres;
    }

    // کپی‌رایت (مثلاً برای فوتر)
    const $copyright = document.getElementById("site-copyright");
    if ($copyright && settings.copy_right_text) {
      $copyright.textContent = settings.copy_right_text;
    }

  } catch (err) {
    console.error("خطا در گرفتن تنظیمات سایت:", err);
  }
})();


