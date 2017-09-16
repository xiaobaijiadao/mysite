var direct =new Array();
$(document).bind("mousewheel",function(event) {   
			position = offsetFunc();
			delta = direct[0]>direct[1] ? 0 : 1;
			console.log(delta, position);

            if (delta == 1){
            	if(position >= -100 && position <= -60){
              		$('#nav-bar').addClass("navbar-fixed-top");
              	}
            }
            else if(delta == 0){
              	if(position >= -100 && position <= -60){
              		$('#nav-bar').removeClass("navbar-fixed-top");
              	}
            } 
        }); 

var offsetFunc = function(){
 		hTop = $('#host-bar').offset();
    	sTop = $(window).scrollTop();
    	hostPos = hTop.top - sTop;
    	if(direct.length === 0){
    		direct[0] = hostPos
    	}else{
    		direct[1] = direct[0];
    		direct[0] = hostPos
    	}
    	return hostPos
}