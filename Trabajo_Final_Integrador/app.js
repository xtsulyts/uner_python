// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Inicializamos las listas de vinos, bodegas y cepas
    const listaVinos = document.getElementById('lista-vinos');
    const listaBodegas = document.getElementById('lista-bodegas');
    const listaCepas = document.getElementById('lista-cepas');

    // Filtros de búsqueda
    const buscadorVinos = document.getElementById('buscador-vinos');
    const buscadorBodegas = document.getElementById('buscador-bodegas');
    const buscadorCepas = document.getElementById('buscador-cepas');

    // Filtros por ID
    const buscadorIdVinos = document.getElementById('buscador-id-vinos');
    const buscadorIdBodegas = document.getElementById('buscador-id-bodegas');
    const buscadorIdCepas = document.getElementById('buscador-id-cepas');

    

    // Función para mostrar las tarjetas
    function mostrarTarjetas(datos, tipo) {
        let listaHTML = '';
        datos.forEach(item => {
            let tarjeta = `<div class="col-12 col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${item.nombre}</h5>
                        <p class="card-text">ID: ${item.id}</p>`;
            
            // Si es un vino, mostramos la bodega y cepas asociadas
            if (tipo === 'vino') {
                tarjeta += `
                    <p class="card-text">Bodega: ${item.bodega}</p>
                    <p class="card-text">Cepas: ${item.cepas.join(', ')}</p>
                    <p class="card-text">Partidas: ${item.partidas.join(', ')}</p>
                `;
            }

            tarjeta += `</div>
                </div>
            </div>`;
            listaHTML += tarjeta;
        });
        // Insertamos las tarjetas en el contenedor adecuado
        if (tipo === 'vino') {
            listaVinos.innerHTML = listaHTML;
        } else if (tipo === 'bodega') {
            listaBodegas.innerHTML = listaHTML;
        } else if (tipo === 'cepa') {
            listaCepas.innerHTML = listaHTML;
        }
    }

    // Función para cargar los datos desde la API
    function cargarDatos(tipo) {
        let url = '';
        if (tipo === 'vino') {
            url = '/api/vinos';
        } else if (tipo === 'bodega') {
            url = '/api/bodegas';
        } else if (tipo === 'cepa') {
            url = '/api/cepas';
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Mostrar las tarjetas con los datos
                mostrarTarjetas(data, tipo);
            })
            .catch(error => {
                console.error('Error al cargar los datos:', error);
            });
    }

    // Función para cargar los datos desde la API
function cargarDatos(tipo) {
    let url = '';

    // Aquí ya no es necesario asignar url según el tipo,
    // porque directamente se va a usar la URL completa de cada recurso
    if (tipo === 'vino') {
        url = 'http://127.0.0.1:5000/api/vinos';  // URL completa
    } else if (tipo === 'bodega') {
        url = 'http://127.0.0.1:5000/api/bodegas';  // URL completa
    } else if (tipo === 'cepa') {
        url = 'http://127.0.0.1:5000/api/cepas';  // URL completa    
    } else if (tipo === 'id') {
        url = 'http://127.0.0.1:5000/api/cepas/id';  // URL completa   
    }


    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Mostrar las tarjetas con los datos
            mostrarTarjetas(data, tipo);
        })
        .catch(error => {
            console.error('Error al cargar los datos:', error);
        });

        
}

    

    // Cargar los datos inicialmente
    cargarDatos('vino');
    cargarDatos('bodega');
    cargarDatos('cepa');

    // Añadir eventos de búsqueda
    buscadorVinos.addEventListener('input', (event) => filtrarResultados(event, 'vino'));
    buscadorBodegas.addEventListener('input', (event) => filtrarResultados(event, 'bodega'));
    buscadorCepas.addEventListener('input', (event) => filtrarResultados(event, 'cepa'));

     // Añadir eventos de búsqueda por ID
     buscadorIdVinos.addEventListener('input', (event) => filtrarResultados(event, 'vino'));
     buscadorIdBodegas.addEventListener('input', (event) => filtrarResultados(event, 'bodega'));
     buscadorIdCepas.addEventListener('input', (event) => filtrarResultados(event, 'cepa'));
});
