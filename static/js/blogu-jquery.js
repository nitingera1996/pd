$(document).ready(function(){
    $('#category_like').click(function(){
		var cat_id;
		cat_id = $(this).attr("data-catid");
		$.get('/blogu/like_category/',{category_id: cat_id},function(data){
		    $('#category_like_count').html(data);
		    $('#category_like').hide();
			});
    });

	$('#blog_like').click(function(){
    //console.log("Hello");
		var blog_id;
		blog_id = $(this).attr("data-blogid");
		$.get('/blogu/like_blog/',{blog_id: blog_id},function(data){
		    $('#blog_like_count').html(data);
		    $('#blog_like').hide();
			});
    });

	$('#suggestion_id').keyup(function(){
    //console.log("Hello");
		var startswith;
		startswith = $(this).val();
		$.get('/blogu/suggest_category/',{query_string: startswith},function(data){
		    $('#cats').html(data);
		});
	});

  $('#suggestion_search').keyup(function(){
    //alert('Hello');
    var search_term;
    search_term=$(this).val();
    //console.log("Hello");
    //alert(search_term);
    $.get('/blogu/search_top/', { query_string : search_term},function(data){
      console.log(data);
      console.log("hello");
      $('#search_results').html(data);
    });
  });

  $('.follow_user').click(function(event){
		var user_id;
		user_id = $(this).attr("data-userprofileid");
		$.get('/blogu/follow_user/',{user_id: user_id},function(data){
		    $("#"+user_id).hide();
			});
    });

  $('.skip').click(function(event){
    var user_id;
    user_id = $(this).attr("data-userprofileid");
    $("#"+user_id).hide();
    });

  $('#profile').click(function() {
  	event.preventDefault();
    $.get('/blogu/add_propic/',function(data){
      $("#profile_data").html(data);
    });
  	var all_div=$('div');
  	all_div.css("opacity",".7");
  	all_div.click(function(event){event.preventDefault();});
  	all_div.keydown(function(event){event.preventDefault();});
  	$('#profile_data').css({"opacity":"1","height":"480px","z-index":"5"});
  	});

  $('li[data-id]').click(function()
  {
    var data_id=$(this).attr("data-id");
    $('div[id^="d"]').css({"z-index":"-2","visibility":"hidden"});
    $("#d"+data_id).css({"z-index":"6","visibility":"visible"});
    $('li[data-id').css({"color":"white","background":"rgb(70,94,170)"});
    $(this).css({"color":"rgb(28,56,110)","background":"white"});
  });
});
