$(document).ready(function(){
    $('#new_comment').hide();
    $('#new_discuss').hide();
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
    if(search_term=="")
    {
      $('#search_results').html("");
    }
     $.ajax({
    type:"GET",
    url: "/blogu/search_top/",
    data: {query_string: search_term},
    success: function(newData){
        console.log(newData);
        $('#search_results').html(newData);
    }
 });
  });

  $('.follow_user').click(function(event){
		var user_id;
		user_id = $(this).attr("data-userprofileid");
		$.get('/blogu/follow_user/',{user_id: user_id},function(data){
		    $("#"+user_id).hide();
			});
    });

  $('#comment').click(function(){
    var user_id,blog_id;
    user_id = $(this).attr("data-uid");
    blog_id = $(this).attr("data-blogid");
    up_name=$(this).attr("data-uname");
    comment_text=$('#comment_text').val();
    $.get('/blogu/comment/',{user_id: user_id,blog_id:blog_id,comment_text:comment_text},function(data){
      $('#new_comment_like').html(data);
      $('#new_comment_text').html(comment_text);
      $('#new_comment_by').html(up_name);
        $('#new_comment').show();
      });
  });

  $('#quick_add_blog').click(function(){
    console.log('Hello');
    var blog_text = $('#quick_blog_text').val();
    console.log(blog_text);
    window.open("/blogu/none/add_blog/","_self");
    console.log('Hello1');
    $('#blog_area').html(blog_text);
  });

  $('#select-category').change(function(){
    var cat_slug = $('#select-category').val();
    console.log('Hello');
    var url= "/blogu/"+ cat_slug + "/add_blog/" ;
    $('#blog_form2').attr("action",url);
  });

  $('#discuss').click(function(){
    var user_id,blog_id;
    up_name=$(this).attr('data-upname');
    user_id = $(this).attr("data-upid");
    discussion_id = $(this).attr("data-discussionid");
    discuss_text=$('#discuss_text').val();
    $.get('/blogu/discuss/',{user_id:user_id,discussion_id:discussion_id,discuss_text:discuss_text},function(data){
      $('#new_discuss_like').html(data);
      $('#new_discuss_text').html(discuss_text);
      $('#new_discuss_by').html(up_name);
        $('#new_discuss').show();
      });
  });

  $('.skip').click(function(event){
    var user_id;
    user_id = $(this).attr("data-userprofileid");
    $("#"+user_id).hide();
    });

  $('#profile_edit').click(function() {
  	event.preventDefault();
    var all_div=$('div');
    all_div.css("opacity",".7");
    all_div.click(function(event){event.preventDefault();});
    all_div.keydown(function(event){event.preventDefault();});
    $('#profile_data').css({"opacity":"1","height":"480px","z-index":"5"});
    $.ajax({
    type:"GET",
    url: "/blogu/add_propic/",
    data: {},
    success: function(newData){
        console.log(newData);
        $('#profile_data').html(newData);
    }
    });
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
