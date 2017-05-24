$(document).ready(function () {
   $(".stacked-menu").click(function(e){
        e.preventDefault();
        $(".nav-item").toggleClass("visible");
   });

   $(window).resize(function() {
        if($(window).width() > 570){
           $(".nav-item").addClass("visible");
        }
   });
});
