/* global App:false */
(function (ns) {
    'use strict';

    ns.views = ns.views || {};


    ns.views.TaskView = Backbone.Marionette.ItemView.extend({
        template: '#task-tpl'
    });

})(App);
