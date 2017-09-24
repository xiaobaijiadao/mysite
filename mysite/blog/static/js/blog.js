$(document).ready(function(){
	$(".response").click(function(){
		var response_author = $(this).next().text();
		var response_id = $(this).next().next().text();
		$("#response2").html("回复&nbsp;"+response_author);
		$("#response1").addClass("hidden");
		$("#response2").removeClass("hidden");
		$("#parent_id").val(response_id);
	});
	$("#deleteResponse").click(function(){
		$("#parent_id").val("0");
		$("#comment_content").val("");
		$("#response2").addClass("hidden");
		$("#response1").removeClass("hidden");	
	});

	$("#comment_form").submit(function(){
		if($("#comment_content").val() == ""){
			$("#warning").removeClass("hidden");
			return false;
		}else{
			return true;
		}
	});

	// $("#submit").click(function(){
	// 	var comment_form = {
	// 		parent_id = $("#parent_id").val(),
	// 		comment_content = $("#comment_content").val(), 
	// 	};
	// 	$("#comment_form").ajax({
	// 		data: comment_form,
	// 		type: "post",
	// 		beforeSend: function(){
	// 			if($("#comment_content").val() == ""){
	// 				$("#warning").removeClass("hidden");
	// 				return false;
	// 			}
	// 			return true;
	// 		},
	// 		success: function(data){
	// 			alert("success");
	// 		},
	// 	})
	// });
});