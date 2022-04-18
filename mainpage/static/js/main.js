define(function () {
    return {
        container: "app",
        rows: [
            {
                view: "toolbar", id: "tb1", cols:
                    [
                        {
                            view: "button", value: "emailer", href: "/emailer", click: function () {
                                window.open(this.config.href);
                            }
                        }
                    ]
            },

            { view: "template", template: "some template" }
        ]
    }
});