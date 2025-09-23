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

(async function loadSliders() {
  try {
    const res = await fetch("/api/v1/sliders/");
    const data = await res.json();

    // خروجی تو آرایه است؛ اگر روزی آبجکت شد هم ساپورت می‌کنیم
    const sliders = Array.isArray(data) ? data : (data.sliders || []);
    if (!sliders.length) return;

    const $sliderContainer = document.querySelector(".hero-slider");
    if (!$sliderContainer) return;

    // ساخت اسلایدها
    $sliderContainer.innerHTML = "";
    sliders.forEach((item) => {
      const slide = document.createElement("div");
      slide.classList.add("hs-item", "set-bg");

      // تصویر: API تو مسیر کامل /media/... می‌دهد و مستقیم قابل استفاده است
      slide.setAttribute("data-setbg", item.image);
      slide.style.backgroundImage = `url(${item.image})`;

      // محتوای داخلی (اختیاری)
      slide.innerHTML = `
        <div class="hs-text">
          ${item.title ? `<h2>${item.title}</h2>` : ""}
          ${item.descriptuon ? `<p>${item.descriptuon}</p>` : ""}
          ${item.url ? `<a href="${item.url}" class="primary-btn">${item.url_title || "مشاهده"}</a>` : ""}
        </div>
      `;

      $sliderContainer.appendChild(slide);
    });

    // اگر قالبت از data-setbg استفاده می‌کند، همین حالا هم style را ست کردیم؛
    // ولی این خط‌ها را می‌گذاریم تا کاملاً سازگار باشد:
    document.querySelectorAll(".set-bg").forEach((el) => {
      const bg = el.getAttribute("data-setbg");
      if (bg) el.style.backgroundImage = `url(${bg})`;
    });

    // این‌جا و فقط این‌جا Owl را init کن؛ چون main.js را برای هِیرو غیرفعال کردیم
    if (window.jQuery && typeof jQuery.fn.owlCarousel === "function") {
      const $owl = jQuery(".hero-slider");
      if ($owl.hasClass("owl-loaded")) {
        $owl.trigger("destroy.owl.carousel");
        $owl.removeClass("owl-loaded");
        $owl.find(".owl-stage-outer").children().unwrap();
      }
      $owl.owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1200,
        animateOut: "fadeOut",
        animateIn: "fadeIn",
        mouseDrag: false,
        autoHeight: false
      });
    }
  } catch (err) {
    console.error("خطا در لود اسلایدر:", err);
  }
})();










