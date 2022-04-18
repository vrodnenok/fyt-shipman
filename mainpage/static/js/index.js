require(['./main'],
    function (main) {
        console.log("this is running");
        webix.ready(function () {
            webix.ui(main);
        });
    });