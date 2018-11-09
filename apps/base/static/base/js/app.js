function changeMenuActiveTab(button) {
    $('.nav-tabs li').removeClass('active');
    $(button).parent().addClass('active');
    console.log('WORK!');
}