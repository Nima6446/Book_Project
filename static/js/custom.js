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

// custom.js — فقط افزودن عنوان، بدون دست‌کاری منطق اسلایدر
(async function loadSliders() {
  try {
    const res = await fetch("/api/v1/sliders/");
    const data = await res.json();

    const sliders = Array.isArray(data) ? data : (data.sliders || []);
    if (!sliders.length) return;

    const $sliderContainer = document.querySelector(".hero-slider");
    if (!$sliderContainer) return;

    // ساخت اسلایدها (مثل قبل) + ایندکس واقعی
    $sliderContainer.innerHTML = "";
    sliders.forEach((item, i) => {
      const slide = document.createElement("div");
      slide.classList.add("hs-item", "set-bg");
      slide.dataset.idx = i;                          // برای تشخیص اسلاید واقعی
      slide.setAttribute("data-setbg", item.image);
      slide.style.backgroundImage = `url(${item.image})`;
      $sliderContainer.appendChild(slide);
    });

    // ست بک‌گراند (مثل قبل)
    document.querySelectorAll(".set-bg").forEach((el) => {
      const bg = el.getAttribute("data-setbg");
      if (bg) el.style.backgroundImage = `url(${bg})`;
    });

    // المان‌های متن
    const $heroTitle = document.getElementById("hero-title");
    const $heroDesc  = document.getElementById("hero-desc");
    const $heroLink  = document.getElementById("hero-link");

    // تابع آپدیت متن‌ها
    function updateContent(idx) {
      const s = sliders[idx] || {};
      if ($heroTitle) $heroTitle.textContent = s.title || "";
      if ($heroDesc)  $heroDesc.textContent  = s.descriptuon || "";
      if ($heroLink) {
        if (s.url) {
          $heroLink.href = s.url;
          $heroLink.textContent = s.url_title || s.title || "مشاهده";
          $heroLink.style.display = "inline-block";
        } else {
          $heroLink.style.display = "none";
        }
      }
    }

    // راه‌اندازی Owl (همان منطق سالم قبلی)
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

      // مقدار اولیه بر اساس آیتم فعالِ فعلی
      (function setInitial() {
        const firstReal = +$owl.find(".owl-item.active .hs-item").data("idx");
        updateContent(Number.isFinite(firstReal) ? firstReal : 0);
      })();

      // با تغییر اسلاید، متن‌ها را با ایندکس واقعی آپدیت کن
      $owl.on("changed.owl.carousel", function (e) {
        const real = +$owl
          .find(".owl-item")
          .eq(e.item.index)
          .find(".hs-item")
          .data("idx");
        const idx = Number.isFinite(real) ? real : (e.item.index % sliders.length);
        updateContent(idx);
      });
    }
  } catch (err) {
    console.error("خطا در لود اسلایدر:", err);
  }
})();















