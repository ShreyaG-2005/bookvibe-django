var swiper=new Swiper(".swiper",{
    effect:"coverflow",
    grabCursor:true,
    centeredSlides:true,
    initialSlide:2,
    speed:600,
    preventClicks: true,
    slidesPerView:"auto",
    coverflowEffect:{
        rotate:0,
        stretch:80,
        depth:350,
        modifier:1,
        slideshows:true,
        },
        on: {
        click(event){
            swiper.slideTo(this.clickedIndex);
        } ,   
        },
        pagination:{
            el:".swiper-pagination",
        },
        loop:true,
        autoplay: {
            delay: 3000, // Time between slides in milliseconds (3000ms = 3 seconds)
            disableOnInteraction: false, // Keeps autoplay running even if user interacts with the swiper
        },
    });
