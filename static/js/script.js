$(function(){
    
    var API = 'https://famedgram.net/ajax/';
    
    //PHOTO DETAİL
    var shortcode = $('.shortcode').val();
    /*
    //COMMENTS
    $.getJSON('https://www.instagram.com/p/'+shortcode+'/?__a=1',function(e){
        $('.postDetail .comments').html('');
        $.each(e.graphql.shortcode_media.edge_media_to_comment.edges,function(i,e){
           var comment = e.node.text;
           var userPic   = e.node.owner.profile_pic_url;
           var userName  = e.node.owner.username;
           
           $('.postDetail .comments').append(`
             <div class="comment">
                <div class="userPic">
                    <img src="${userPic}"/>
                </div>
                <div class="userName">
                    ${userName}
                </div>
                <div class="userText">
                ${comment}
                </div>
            </div>
           `);
           
        });
       
    });
    //COMMENTS
    */
    //PHOTO DETAİL
    
    //PROFIL POST CHECK
    if($('.page').hasClass('profile-detail')){
        var username = $('input.username').val();
        var userID = $('input.userID').val();
        
        $.get('https://www.instagram.com/'+username,function(e){
            
            $.post(API+'profile-detail.php',{data:e,username:username,userID:userID},function(e){
                //location.reload();
            });
            
        });
        
    }
    //PROFIL POST CHECK
    
    //PROFIL POST DETAIL CHECK
    /*
    if($('.page').hasClass('post-detail')){
        
        var username = $('input.username').val();
        var userID = $('input.userID').val();
        var postID = $('input.postID').val();
        
        $.get('https://www.instagram.com/p/'+postID,function(e){
            
            $.post(API+'post-detail.php',{data:e,username,userID,postID},function(e){
                //location.reload();
            });
            
        });
        
    }
    */
    //PROFIL POST DETAIL CHECK
    
    
    //LIGHTBOX
    var lightbox = new Lightbox();
 	lightbox.load();
    //LIGHTBOX
});