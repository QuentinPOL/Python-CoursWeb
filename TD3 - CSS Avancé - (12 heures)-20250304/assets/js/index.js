$("ul li").click(function(event) {
    var loc = $(this).find("a").first().attr("href");
    if(loc !== undefined) {
        window.location.href = loc;
    }
});