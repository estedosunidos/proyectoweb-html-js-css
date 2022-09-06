$(document).ready(function () {
    // slider
    $('.bxslider').bxSlider({
        mode: 'fade',
        captions: true,
        slideWidth: 600,
        responsive: true,
        pager: false
    });
    //post
    var posts = [
        {
            title: 'prueba de titulo1',
            date: new Date(),
            content: 'Lorem'
        },
        {
            title: 'prueba de titulo2',
            date: new Date(),
            content: 'Lorem'
        },
        {
            title: 'prueba de titulo3',
            date: new Date(),
            content: 'Lorem'
        }
        ,
        {
            title: 'prueba de titulo4',
            date: new Date(),
            content: 'Lorem'
        }
    ]

    posts.forEach((item, index) => {
        var post = `
                <h2>${item.title}</h2>
                <span class="fecha">${item.date} </span>
                <h1>Lorem ipsum </h1>
                <p>
                     ${item.content}
                </p>
  `
        $("#posts").append(post)
    })

    //selecto tema

    var theme = $("#theme")

    $("#to-blue").click(function () {
        theme.attr("href", "C:/Users/ested/Desktop/Proyecto html,js,css/css/blue.css")

    })

    $("#to-red").click(function () {
        theme.attr("href", "C:/Users/ested/Desktop/Proyecto html,js,css/css/red.css")

    })

    $("#to-gree").click(function () {
        theme.attr("href", "C:/Users/ested/Desktop/Proyecto html,js,css/css/green.css")

    })

    // scrooll
    var a = $(".up")
    a.click(function(){
        e.preventdefault()
        $('html,body').animate({
            scrollTop: 0
        },500)
        return false
    })
})

