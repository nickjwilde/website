$(document).ready(function () {
   $(".stacked-menu").click(function(e){
        e.preventDefault();
        if($(".nav-item").hasClass("visible")){
            $(".nav-item").removeClass("visible");
        }else{
            $(".nav-item").addClass("visible");
        }
   });

   $(window).resize(function() {
        if($(window).width() > 570){
           $(".nav-item").addClass("visible");
        }
        else{
           $(".nav-item").removeClass("visible");
        }
   });
});
