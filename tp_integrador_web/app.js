// Base URL del backend
const BASE_URL = "http://127.0.0.1:5000/api";

// Función para cargar y mostrar los vinos
async function loadVinos() {
    const response = await fetch(`${BASE_URL}/vinos`);
    const data = await response.json();
    displayList(data.vinos, 'vinos');
}

// Función para cargar y mostrar las bodegas
async function loadBodegas() {
    const response = await fetch(`${BASE_URL}/bodegas`);
    const data = await response.json();
    displayList(data.bodegas, 'bodegas');
}

// Función para cargar y mostrar las cepas
async function loadCepas() {
    const response = await fetch(`${BASE_URL}/cepas`);
    const data = await response.json();
    displayList(data.cepas, 'cepas');
}

// Función para mostrar una lista en el contenedor
function displayList(items, type) {
    const container = document.getElementById('list-container');
    container.innerHTML = ''; // Limpiar el contenido previo

    items.forEach(item => {
        const div = document.createElement('div');
        div.textContent = `ID: ${item.id}, Nombre: ${item.nombre}`;
        div.dataset.id = item.id;
        div.dataset.type = type;

        div.addEventListener('click', () => {
            loadItemDetail(type, item.id);
        });

        container.appendChild(div);
    });
}

// Función para cargar detalles por ID
async function loadDetail() {
    const id = document.getElementById('id-input').value;
    const type = document.getElementById('type-select').value;

    if (!id) {
        alert('Por favor, ingrese un ID.');
        return;
    }

    loadItemDetail(type, id);
}

// Función para cargar un elemento específico por ID
async function loadItemDetail(type, id) {
    const response = await fetch(`${BASE_URL}/${type}/${id}`);
    if (!response.ok) {
        alert(`No se encontró un ${type.slice(0, -1)} con el ID proporcionado.`);
        return;
    }
    const data = await response.json();
    displayCard(data);
}

// Función para mostrar el detalle en una tarjeta
function displayCard(item) {
    const container = document.getElementById('card-container');
    container.innerHTML = `
        <h3>Detalle</h3>
        <pre>${JSON.stringify(item, null, 2)}</pre>
    `;
}
