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
    console.log('load all tasks');
}

function loadOpenTasks() {
    console.log('load open tasks');
}

function loadInProgressTasks() {
    console.log('load in progress tasks');
}

function loadFinishedTasks() {
    console.log('load finished tasks');
}

function acceptTask() {
    console.log('accept');
}

function finishTask() {
    console.log('finish');
}