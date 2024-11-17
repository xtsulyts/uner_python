document.addEventListener("DOMContentLoaded", function () {
    // Se seleccionan los elementos de entrada para cada tipo de búsqueda
    const buscadorVinosId = document.getElementById('buscador-vinos-id');
    const buscadorBodegasId = document.getElementById('buscador-bodegas-id');
    const buscadorCepasId = document.getElementById('buscador-cepas-id');

    // Se seleccionan las secciones de las listas para vinos, bodegas y cepas
    const listaVinos = document.getElementById('lista-vinos');
    const listaBodegas = document.getElementById('lista-bodegas');
    const listaCepas = document.getElementById('lista-cepas');

    // Función para mostrar las tarjetas con los datos obtenidos    
    function mostrarTarjetas(datos, tipo) {
        let listaHTML = '';
        datos.forEach(item => {
            let tarjeta = `
                <div class="col-12 col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${item.nombre}</h5>
                            <p class="card-text">ID: ${item.id}</p>
            `;
            if (tipo === 'vino') {
                tarjeta += `
                    <p class="card-text">Bodega: ${item.bodega}</p>
                    <p class="card-text">Cepas: ${item.cepas.join(', ')}</p>
                    <p class="card-text">Partidas: ${item.partidas.join(', ')}</p>
                `;
            }
            tarjeta += `
                        </div>
                    </div>
                </div>
            `;
            listaHTML += tarjeta;
        });

        // Actualizamos el DOM con las tarjetas correspondientes
        if (tipo === 'vino') {
            listaVinos.innerHTML = listaHTML;
        } else if (tipo === 'bodega') {
            listaBodegas.innerHTML = listaHTML;
        } else if (tipo === 'cepa') {
            listaCepas.innerHTML = listaHTML;
        }
    }


    // Función para cargar los datos de un tipo específico (vinos, bodegas, cepas)
    function cargarDatos(tipo) {
        let url = '';
        if (tipo === 'vino') {
            //buscadorVinosId.innerHTML = listaHTML;
            url = 'http://127.0.0.1:5000/api/vinos';  // URL para obtener todos los vinos
        } else if (tipo === 'bodega') {
            url = 'http://127.0.0.1:5000/api/bodegas';  // URL para obtener todas las bodegas
        } else if (tipo === 'cepa') {
            url = 'http://127.0.0.1:5000/api/cepas';  // URL para obtener todas las cepas
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Ver los datos en la consola
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
   


    // Añadir eventos de búsqueda para cada campo de ID
    buscadorVinosId.addEventListener('input', (event) => {
        console.log(`Input en vino: ${event.target.value}`);  // Agregado para depuración
        buscarPorId(event.target.value, 'vino');
    });

    buscadorBodegasId.addEventListener('input', (event) => {
        console.log(`Input en bodega: ${event.target.value}`);  // Agregado para depuración
        buscarPorId(event.target.value, 'bodega');
    });

    buscadorCepasId.addEventListener('input', (event) => {
        console.log(`Input en cepa: ${event.target.value}`);  // Agregado para depuración
        buscarPorId(event.target.value, 'cepa');
    });
});
