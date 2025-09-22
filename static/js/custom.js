//site header
(async function loadSiteSettings() {
    try {
        // مسیر API رو مطابق urls خودت بذار
        const res = await fetch("/api/v1/settings/");
        const data = await res.json();

        if (!data.settings) return;
        const settings = data.settings;

        // header logo
        const $logo = document.getElementById("site-logo");
        if ($logo && settings.site_logo) {
            $logo.src = settings.site_logo;
            $logo.alt = settings.site_name || "Site Logo";
        }
        // footer logo
        const $footer_Logo = document.getElementById("footer-logo");
        if ($footer_Logo && settings.site_logo) {
            $footer_Logo.src = settings.site_logo;
            $footer_Logo.alt = settings.site_name || "Footer Logo";
        }


        // header tell
        const $tell = document.getElementById("site-tell");
        if ($tell && settings.tell) {
            const tel = settings.tell.trim();
            $tell.textContent = tel;
            $tell.href = "tel:" + tel.replace(/\s+/g, "");
        }

        // footer tell
        const $foote_rtell = document.getElementById("site-footer-tell");
        if ($foote_rtell && settings.tell) {
            const tel = settings.tell.trim();
            $foote_rtell.textContent = tel;
            $foote_rtell.href = "tel:" + tel.replace(/\s+/g, "");
        }

        // header email
        const $email = document.getElementById("site-email");
        if ($email && settings.email) {
            const mail = settings.email.trim();
            $email.textContent = mail;
            $email.href = "mailto:" + mail;
        }

        // footer email
        const $header_email = document.getElementById("site-footer-email");
        if ($header_email && settings.email) {
            const mail = settings.email.trim();
            $header_email.textContent = mail;
            $header_email.href = "mailto:" + mail;
        }

        // address
        const $address = document.getElementById("site-address");
        if ($address && settings.addres) {
            $address.textContent = settings.addres;
        }

        // copy_right
        const $copyright = document.getElementById("site-copyright");
        if ($copyright && settings.copy_right_text) {
            $copyright.textContent = settings.copy_right_text;
        }
        // about_us
        const $about_us_page = document.getElementById("site-about-us-page");
        if ($about_us_page && settings.about_us_page) {
            $about_us_page.textContent = settings.about_us_page;
        }

    } catch (err) {
        console.error("خطا در گرفتن تنظیمات سایت:", err);
    }
})();

document.addEventListener("DOMContentLoaded", async function () {
  try {
    const res = await fetch("/api/v1/sliders/");
    const sliders = await res.json();

    const heroSlider = document.querySelector(".hero-slider");
    if (!heroSlider) return;

    heroSlider.innerHTML = ""; // پاک کردن اسلایدهای استاتیک

    sliders.forEach(slide => {
      const div = document.createElement("div");
      div.classList.add("hs-item", "set-bg");
      div.setAttribute("data-setbg", slide.image);

      // متن داخل اسلاید (اگه خواستی عنوان/توضیحات هم بیاد)
      div.innerHTML = `
        <div class="hs-text">
          <h2>${slide.title}</h2>
          <p>${slide.descriptuon}</p>
          ${slide.url ? `<a href="${slide.url}" class="primary-btn">${slide.url_title}</a>` : ""}
        </div>
      `;

      heroSlider.appendChild(div);
    });

    // چون قالب از data-setbg استفاده می‌کنه برای بک‌گراند
    document.querySelectorAll(".set-bg").forEach(el => {
      const bg = el.getAttribute("data-setbg");
      if (bg) {
        el.style.backgroundImage = `url(${bg})`;
      }
    });

    // اگر داری از OwlCarousel استفاده می‌کنی باید دوباره initialize بشه
    if (typeof $ !== "undefined" && $(".hero-slider").owlCarousel) {
      $(".hero-slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1200,
        animateOut: "fadeOut"
      });
    }

  } catch (err) {
    console.error("خطا در گرفتن اسلایدها:", err);
  }
});





