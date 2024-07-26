document.addEventListener('DOMContentLoaded', () => {

	new WOW({
		mobile: false
	}).init();

	// Preloader START
	var preloader = document.getElementById('preloader-container');
	var progressBar = document.getElementById('preloader-bar');
    var content = document.getElementById('content');
    var interval = setInterval(updateProgress, 50);
    var width = 0;

    function updateProgress() {
        if (width >= 100) {
            clearInterval(interval);
            progressBar.style.width = '100%';
            progressBar.style.display = 'none';
            preloader.classList.add('is-hidden');
			setTimeout(function() {
                preloader.style.display = 'none';
            }, 500);
        } else {
            width += 1; // Вы можете настроить скорость увеличения
            progressBar.style.width = width + '%';
        }
    }
    $('.preloader-close').on('click', function() {
		preloader.classList.add('is-hidden');
    });
	// Preloader START

	// Contact Form Send START
	$('.ajax-form').on('submit', function() { 
		var th = $(this);
		$.ajax({
			type: 'POST',
			url: 'mail.php',
			data: th.serialize(),
			success: function() {
				th.trigger('reset');
				$.magnificPopup.open({
					items: {
						src: '<div class="form-alert"><p>Your application has been successfully sent. <br> Expect a call!</p></div>',
						type: 'inline'
					},
					mainClass: 'mfp-fade',
					removalDelay: 160,
					preloader: true,
					fixedContentPos: false,
				});
			},
			error: function() {
				th.trigger('reset');
				$.magnificPopup.open({
					items: {
						src: '<div class="form-alert"><p>An error occurred, please try again</p></div>',
						type: 'inline'
					},
					mainClass: 'mfp-fade',
					removalDelay: 160,
					preloader: true,
					fixedContentPos: false,
				});
			}
		});
		return false;
	});
	// Contact Form Send END

	// Global Scripts START
	$('.magnific-iframe').magnificPopup({
		type: 'iframe',
		mainClass: 'mfp-fade',
        removalDelay: 160,
		preloader: false,
        fixedContentPos: false
	});

	$('.magnific-image').magnificPopup({
		type: 'image',
		mainClass: 'mfp-fade',
        removalDelay: 160,
		preloader: true,
		gallery: {
			enabled: true
		}
	});

	$('.magnific-inline').magnificPopup({
		type: 'inline',
		mainClass: 'mfp-fade',
        removalDelay: 160,
		preloader: true,
        fixedContentPos: false,
	});
	// Global Scripts END

	// Header START
	$('.hamburger').on('click', function() {
		var headerMobile = $('.header-mobile-wrap');
		headerMobile.addClass('is-active');
	});
	$('.header-mobile-close').on('click', function() {
		var headerMobile = $('.header-mobile-wrap');
		headerMobile.removeClass('is-active');
	});
	$('.menu-open-arrow').on('click', function() {
		var submenu = $(this).next('.sub-menu');
		
		if(submenu.hasClass('is-active')) {
			$(this).removeClass('is-active');
			submenu.removeClass('is-active');
			submenu.slideUp('500');
		}
		else {
			$(this).addClass('is-active');
			submenu.addClass('is-active');
			submenu.slideDown('500');
		}
	});
	// Header END

	// Search START
	var searchWrap = $('.search-wrap');
	var addonWrap = $('.addon-wrap');
	var backdrop = $('.backdrop');
	$('.search-btn-js').on('click', function() {
		searchWrap.addClass('is-active');
		addonWrap.removeClass('is-active');
	})
	$('.search-close').on('click', function() {
		searchWrap.removeClass('is-active');
	})
	// Search END

	// Addon START
	$('.addon-btn-js').on('click', function() {
		addonWrap.addClass('is-active');
		backdrop.addClass('is-active');
		searchWrap.removeClass('is-active');
	});
	$('.addon-close').on('click', function() {
		addonWrap.removeClass('is-active');
		backdrop.removeClass('is-active');
	})
	$(document).on('mouseup', function(e) { 
		if ( !addonWrap.is(e.target) && addonWrap.has(e.target).length === 0 ) { 
			addonWrap.removeClass('is-active');
			backdrop.removeClass('is-active');
		}
	});
	// Addon END

	// Cursor START
	const cursor = document.getElementById('cursor');
    const cursorSize = cursor.offsetWidth;
    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.pageX - cursorSize / 2;
        mouseY = e.pageY - cursorSize / 2;
    });

    function lerp(start, end, t) {
        return start * (1 - t) + end * t;
    }

    function animate() {
        cursorX = lerp(cursorX, mouseX, 0.1);
        cursorY = lerp(cursorY, mouseY, 0.1);

        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';

        requestAnimationFrame(animate);
    }

    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('mouseenter', () => {
            cursor.classList.add('is-link');
        });

        link.addEventListener('mouseleave', () => {
            cursor.classList.remove('is-link');
        });
    });

    animate();
	// Cursor END

	// Banner START
	const swiperBanner = new Swiper('.swiper-banner', {
		speed: 1000,
		parallax: true,
		allowTouchMove: true,
		autoplay: {
			delay: 7000,
			disableOnInteraction: true,
		},
		navigation: {
			prevEl: '.swiper-banner .swiper-button-prev',
			nextEl: '.swiper-banner .swiper-button-next',
		},
		on: {
			init: function () {
			  updateNavigationImages(this);
			},
			slideChange: function () {
			  updateNavigationImages(this);
			},
		  },
		pagination: {
			el: '.swiper-banner .swiper-pagination',
			clickable: true,
		},
	});

	function updateNavigationImages(swiper) {
        const slides = swiper.slides;
        const totalSlides = slides.length;
        const activeIndex = swiper.activeIndex;
        const prevIndex = (activeIndex - 1 + totalSlides) % totalSlides;
        const nextIndex = (activeIndex + 1) % totalSlides;

        const getBackgroundImageUrl = (element) => {
          const backgroundImage = window.getComputedStyle(element).backgroundImage;
          return backgroundImage.slice(5, -2);
        };

        const prevImgElement = slides[prevIndex].querySelector('.banner-content');
        const nextImgElement = slides[nextIndex].querySelector('.banner-content');

        const navPrevButton = document.querySelector('.swiper-button-prev');
        const navNextButton = document.querySelector('.swiper-button-next');

        if (prevImgElement) {
          const prevImgSrc = getBackgroundImageUrl(prevImgElement);
          navPrevButton.classList.add('is-active');
          setTimeout(() => {
            navPrevButton.querySelector('img').src = prevImgSrc;
            navPrevButton.classList.remove('is-active');
          }, 500);
        }
        if (nextImgElement) {
          const nextImgSrc = getBackgroundImageUrl(nextImgElement);
          navNextButton.classList.add('is-active');
          setTimeout(() => {
            navNextButton.querySelector('img').src = nextImgSrc;
            navNextButton.classList.remove('is-active');
          }, 500);
        }
      }
	// Banner END


	// Number counter START
	function isScrolledIntoView(elem) {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(elem).height();

        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    }

    function countUp($element) {
        var countTo = $element.data('count');
        $({ countNum: $element.text() }).animate({
            countNum: countTo
        },
        {
            duration: 3000,
            easing: 'swing',
            step: function() {
                $element.text(Math.floor(this.countNum));
            },
            complete: function() {
                $element.text(this.countNum);
            }
        });
    }

	function scrollUpShow() {
		if($(this).scrollTop() > 700) {
			$('.scroller-wrap').addClass('is-active');
		}
		else {
			$('.scroller-wrap').removeClass('is-active');
		}
	}
	scrollUpShow();

    var counted = false;
    $(window).on('scroll', function() {
        var $numScroll = $('.num-scroll');
        if ($numScroll.length && isScrolledIntoView($numScroll) && !counted) {
            $('.num-js').each(function() {
                countUp($(this));
            });
            counted = true;
        }

		// Scroller START
		scrollUpShow();
		let scrollTop = $(window).scrollTop();
		let docHeight = $(document).height();
		let winHeight = $(window).height();

		let scrollPercent = (scrollTop / (docHeight - winHeight)) * 100;
		scrollPercent = Math.round(scrollPercent);

		$('.scroller-percent').text(scrollPercent + '%');
		// Scroller END
    });

	$('#scroller-up').on('click', function() {
		$('html, body').animate({ scrollTop: 0 }, 'slow');
	});

	$('#scroller-down').on('click', function() {
		$('html, body').animate({ scrollTop: $(document).height() }, 'slow');
	});
	// Number counter END

	// Features START
	const image = document.querySelector('.features-img img');
	
	document.addEventListener('mousemove', function(e) {
		if(image) {
			const x = e.clientX;
			const y = e.clientY;
			const windowWidth = window.innerWidth;
			const windowHeight = window.innerHeight;
			const centerX = windowWidth / 2;
			const centerY = windowHeight / 2;
			const deltaX = (x - centerX) / centerX;
			const deltaY = (y - centerY) / centerY;
			const sensitivity = 10;
	
			const translateX = deltaX * sensitivity;
			const translateY = deltaY * sensitivity;
	
			image.style.transform = `translate(${translateX}px, ${translateY}px)`;
		}
	});
	// Features END

	// Services START
	const swiperServices = new Swiper('.swiper-services', {
		speed: 1000,
		spaceBetween: 20,
		autoplay: {
			delay: 3200,
		},
		scrollbar: {
			el: '.swiper-services .swiper-scrollbar',
			draggable: true,
			dragSize: 62,
		},
		pagination: {
			el: '.swiper-services .swiper-pagination',
			clickable: true,
		},
		mousewheel: {
			enabled: false
		},
		breakpoints: {
			0: {
				slidesPerView: 1,
			},
			520: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 4,
			},
		}
	});
	// Services END

	// Works START
	const swiperWorks = new Swiper('.swiper-works', {
		speed: 1000,
		slidesPerView: 4,
		scrollbar: {
			el: '.swiper-works .swiper-scrollbar',
			draggable: true,
			dragSize: 62,
		},
		breakpoints: {
			0: {
				slidesPerView: 1,
			},
			520: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 4,
			},
		}
	});

	// Init Masonry
	var $grid = $('.masonry-grid').masonry({
		itemSelector: '.grid-item',
		columnWidth: '.grid-sizer',
		percentPosition: true,
		gutter: 20
	})
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout');
	});
	// Works END

	// News START
	const swiperNews = new Swiper('.swiper-news', {
		speed: 1000,
		slidesPerView: 'auto',
		spaceBetween: 20,
		pagination: {
			el: '.swiper-news .swiper-pagination',
			clickable: true,
		},
	});
	// News END

	// Reviews START
	const swiperReviews = new Swiper('.swiper-reviews', {
		speed: 1000,
		slidesPerView: 1,
		spaceBetween: 20,
		direction: 'vertical',
		scrollbar: {
			el: '.swiper-reviews .swiper-scrollbar',
			draggable: true,
			dragSize: 62,
		},
		mousewheel: {
			enabled: true
		},
	});
	// Reviews END

	// Partners START
	const swiperPartners = new Swiper('.swiper-partners', {
		speed: 1000,
		spaceBetween: 10,
		autoplay: {
			delay: 3000,
		},
		breakpoints: {
			0: {
				slidesPerView: 2,
			},
			520: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 5,
			},
		}
	});
	// Partners END

	// FAQ START
	$('.faq-question').click(function() {
		var accordionItem = $(this).closest('.faq-item');
		if (accordionItem.hasClass('active')) {
			accordionItem.removeClass('active');
			accordionItem.find('.faq-answer').slideUp();
		} else {
			$('.faq-item').removeClass('active');
			$('.faq-answer').slideUp();
			accordionItem.addClass('active');
			accordionItem.find('.faq-answer').slideDown();
		}
	});
	// FAQ END

	// About START
	var animationDone = false;

    function startProgress() {
        if (animationDone) return;

        if ($('.progress-js').length) {
            var skillsTop = $('.progress-js').offset().top;
        }
        if ($(window).scrollTop() >= skillsTop) {
            $('.progress-drag').each(function() {
                var $this = $(this);
                var percentNum = $this.closest('.progress-item').find('.progress-percent').data('percent');
                
                $({numberValue: 0}).animate({numberValue: percentNum}, {
                    duration: 1500,
                    easing: 'linear',
                    step: function() {
                        var roundedValue = Math.floor(this.numberValue);
                        $this.closest('.progress-item').find('.progress-percent').text(roundedValue + '%');
                        $this.width(roundedValue + '%');
                    },
                    complete: function() {
                        $this.closest('.progress-item').find('.progress-percent').text(percentNum + '%');
                        $this.width(percentNum + '%');
                    }
                });
            });

            animationDone = true;
        }
    }

	startProgress();
	$(window).on('scroll', function() {
		startProgress();
	});
	// About END

	// Works START
	$('.works-tab-item a').on('click', function(e) {
        e.preventDefault();
        var currentAttrValue = $(this).attr('href');

		$('.works-tab li').removeClass('is-active');
		$(this).parent('li').addClass('is-active');

		$('.works-tab-content').removeClass('is-active');
		$(currentAttrValue).addClass('is-active');
		
    });
	// Works END
	
})