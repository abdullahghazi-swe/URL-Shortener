const urlList = document.querySelector('.url-list');

urlList?.addEventListener('click', e => {
    const btn = e.target.closest('.actions');

    if (!btn) return;
    e.preventDefault();

    const activeDropDown = document.querySelector('.drop-down.show');
    if (activeDropDown) {
        activeDropDown.classList.remove('show');
    }

    const id = btn.dataset.id
    const dropdown = document.getElementById(`menu-${id}`)

    if (activeDropDown === dropdown) return;
    dropdown.classList.add('show');
})

document.addEventListener('click', e => {
    const dropDown = e.target.closest('.drop-down')
    const btn = e.target.closest('.actions')

    if (dropDown || btn) return;

    const activeDropDown = document.querySelector('.drop-down.show');
    if (activeDropDown) {
        activeDropDown.classList.remove('show');
    }
})