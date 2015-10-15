$(document).ready(function(){
    $('#new_comment').hide();
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
    /*$.get('/blogu/search_top/',{ query_string : search_term},function(data){
      console.log(data);
      console.log("hello");
      $('#search_results').html(data);
    });*/
     $.ajax({
    type:"GET",
    url: "/blogu/search_top/",
    data: {query_string: search_term},
    success: function(newData){
        $('#search_results').html(newData);
    }
 });
  });

  $('#follow_user').click(function(){
		var user_id;
		user_id = $(this).attr("data-userprofileid");
		$.get('/blogu/follow_user/',{user_id: user_id},function(data){
		    $('#follow_user').hide();
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

});
