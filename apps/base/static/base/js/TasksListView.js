/* global App:false */
(function (ns) {
    'use strict';

    ns.views = ns.views || {};


    ns.views.TasksCollectionView = Backbone.Marionette.CollectionView.extend({
        childView: ns.views.TaskView
    });


    ns.views.TasksListView = Backbone.Marionette.LayoutView.extend({

        regions: {
            tasks: ''
        },

        initialize: function (options) {
            if (options && options.el) {
              this.bindUIElements();
              this.triggerMethod('render', this);
            }

            this.collection = new ns.collections.Tasks();
        },

        onRender: function () {
            // show here collection view?
        }
    });


})(App);
