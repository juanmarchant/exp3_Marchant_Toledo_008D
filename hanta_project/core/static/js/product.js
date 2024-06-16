const modalProduct = new bootstrap.Modal(document.getElementById('modalProduct'), {});

cargarEventListeners();

function cargarEventListeners() {
    document.addEventListener('DOMContentLoaded', fetchData);
}

function fetchData() {
    const url = 'http://localhost:3000/games'
    fetch(url)
        .then(answer => answer.json())
        .then(data => showDataHTMl(data))
}

function showDataHTMl(games = []) {

    const container = document.querySelector('#gamesGrid');
    cleanHtml(container);

    console.log(games);
    games.forEach(game => {
        const column = document.createElement('DIV');
        column.classList.add('col', 'rounded', 'p-3')

        const columnBody = document.createElement('DIV')
        columnBody.classList.add('shadow', 'rounded', 'product')

        columnBody.innerHTML =
            `
        <img src="${game.HEAD_IMAGE}" class="w-100 rounded-top " alt="">
        <div class="p-2 rounded-bottom border-top-orange">
            <h5 class="text-start text-truncate">${game.GAMES}</h5>
            <p class="card-text text-truncate text-uppercase fw-bold th-blue"
                style="max-width: 100%;">
                GLOBAL
            </p>
            <p class="fw-bold fs-4 text-start price">${game.OUR_PRICE} USD</p>
        </div>
        `
        column.onclick = function () {
            mostrandoProducto(game);
        }
        column.appendChild(columnBody)
        container.appendChild(column)
    })
}

function mostrandoProducto(data) {

    // const { nombre, descripcion, portada, imagenes, precio } = data;

    const titleModal = document.querySelector('.modal-header h5');
    titleModal.textContent = data.GAMES;

    const portadaModal = document.querySelector('#portada');
    portadaModal.innerHTML =
        `
        <img class="img-fluid w-100 mx-auto rounded shadow-lg "
        src="${data.HEAD_IMAGE}"
        alt="">
        `

    const descriptionModal = document.querySelector('.modal-body #description');
    descriptionModal.innerHTML = data.DESCRIPTION

    const modalBody = document.querySelector('#screenshots');

    cleanHtml(modalBody);

    // Image 1
    const colImgModalOne = document.createElement('DIV')
    colImgModalOne.classList.add('col')
    colImgModalOne.innerHTML =
        `
    <a href="${data.IMAGE_1}"
        target="_blank">
        <img class="img-fluid rounded "
            src="${data.IMAGE_1}"
            alt="">
    </a>
    `

    const colImgModalTwo = document.createElement('DIV')
    colImgModalTwo.classList.add('col')
    colImgModalTwo.innerHTML =
        `
        <a href="${data.IMAGE_2}"
            target="_blank">
            <img class="img-fluid rounded "
                src="${data.IMAGE_2}"
                alt="">
        </a>
        `
    const colImgModalThree = document.createElement('DIV')
    colImgModalThree.classList.add('col')
    colImgModalThree.innerHTML =
        `
        <a href="${data.IMAGE_3}"
            target="_blank">
            <img class="img-fluid rounded "
                src="${data.IMAGE_3}"
                alt="">
        </a>
        `

    const colImgModalFour = document.createElement('DIV')
    colImgModalFour.classList.add('col')
    colImgModalFour.innerHTML =
        `
        <a href="${data.IMAGE_4}"
            target="_blank">
            <img class="img-fluid rounded "
                src="${data.IMAGE_4}"
                alt="">
        </a>
        `
    modalBody.appendChild(colImgModalOne)
    modalBody.appendChild(colImgModalTwo)
    modalBody.appendChild(colImgModalThree)
    modalBody.appendChild(colImgModalFour)

    const priceModal = document.querySelector('#price')
    priceModal.textContent = `${data.OUR_PRICE} USD`

    modalProduct.show()
}

function cleanHtml(position) {
    while (position.firstChild) {
        position.removeChild(position.firstChild)
    }
}