const urlList = document.querySelector('.url-list');
const deleteBtn = document.querySelector('#deleteBtn');
const deleteModal = document.querySelector('.delete-modal')
const cancelDel = document.querySelector('.cancel-btn')

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
    if (btn) return;

    if (dropDown) {

        const actionBtn = e.target.closest("button")
        if (actionBtn.dataset.action === 'copy') {
            const link = e.target.closest('.link').querySelector('.short-url')
            try {
                navigator.clipboard.writeText(link.textContent)
            } catch {
                console.error("Couldnt Copy link:", err)
            }
        } else {
            return;
        }
    }

    const activeDropDown = document.querySelector('.drop-down.show');
    if (activeDropDown) {
        activeDropDown.classList.remove('show');
    }
})

deleteBtn?.addEventListener('click', e => {
    if (deleteModal) {
        deleteModal.classList.add('show');
    }
})

deleteModal?.addEventListener('click', e => {

    if (e.target === deleteModal) {
        closeModal();
    }
})

cancelDel?.addEventListener('click', closeModal)

function closeModal() {
    deleteModal?.classList.remove('show')
}