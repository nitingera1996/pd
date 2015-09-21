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
});
