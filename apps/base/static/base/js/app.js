function changeMenuActiveTab(button) {
    $('.nav-tabs li').removeClass('active');
    $(button).parent().addClass('active');

    const selectedTab = $(button).text();
    switch (selectedTab) {
        case 'Все заказы':
            loadAllTasks();
            break;
        case 'Ожидающие':
            loadOpenTasks();
            break;
        case 'Принятые':
            loadInProgressTasks();
            break;
        case 'Выполненные':
            loadFinishedTasks();
            break;
    }
}

function loadAllTasks() {
    $.get('/get_all_tasks/', function(data) {
        $('#app ul').html(createTasksList(data['tasks']));
        $('body').css('opacity', 1);
    });
}

function loadOpenTasks() {
    $.get('/get_open_tasks/', function(data) {
        $('#app ul').html(createTasksList(data['tasks']));
        $('body').css('opacity', 1);
    });
}

function loadInProgressTasks() {
    $.get('/get_in_progress_tasks/', function(data) {
        $('#app ul').html(createTasksList(data['tasks']));
        $('body').css('opacity', 1);
    });
}

function loadFinishedTasks() {
    $.get('/get_finished_tasks/', function(data) {
        $('#app ul').html(createTasksList(data['tasks']));
        $('body').css('opacity', 1);
    });
}

function acceptTask(id) {
    console.log('accept task ' + id);
}

function finishTask(id) {
    console.log('finish task ' + id);
}

function createTasksList(tasks) {
    html_text = '';

    tasks.forEach(function (item) {
        html_text += createTaskCard(item);
    });

    return html_text
}

function createTaskCard(task_json) {
    const id = task_json['id'];
    const text = task_json['text'];
    const link = task_json['link'];
    const link_slice = link.slice(0, 60) + '...';
    const price = task_json['price'];
    const status = task_json['status'];

    var status_badge_html = '';
    var button_html = '';

    if (status === 1) {
        status_badge_html = `<span class="label label-info">Ожидает</span>`;
        button_html = `
<button type="button" class="btn btn-primary" onclick="acceptTask(` + id + `)">
  Принять
</button>`;
    } else if (status === 20) {
        status_badge_html = `<span class="label label-warning">Принято</span>`;
        button_html = `
<button type="button" class="btn btn-success" onclick="finishTask(` + id + `)">
  Выполнить
</button>`;
    } else {
        status_badge_html = `<span class="label label-success">Выполнено</span>`;
        button_html = '';
    }

    return `
<li>
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title"> Заказ #` + id + `</h3>
    ` + status_badge_html + `
  </div>
  <div class="panel-body">
    <div class="task-description">
      <p>` + text + `</p>
      <a href=" ` + link + ` "> ` + link_slice + `</a>
     </div>
     <div class="task-action">
       <p class="price-info">Стоимость: <strong> ` + price + `</strong></p>
       ` + button_html + `
      </div>
   </div>
</div>
</li>`;

}

$(document).ready(function() {
    loadAllTasks();
});