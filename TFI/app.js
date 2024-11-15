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


    function buscarPorId(id, ids) {
        
        const url = `http://127.0.0.1:5000/api/${id}/${ids}`; // URL específica para el tipo e ID  
         fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`No se encontró el ID ${id}`);
                }
                return response.json();
            })
            .then(data => {
                console.log(`Datos recibidos con ID ${id}:`, data);
                // Llama a la función para mostrar esta tarjeta con un estilo único
                mostrarTarjetaIndividual(data, tipo);
            })
            .catch(error => {
                console.error('Error en la búsqueda por ID:', error);
                alert(error.message); // Muestra un mensaje si el ID no existe o hay error
            });
    }

    function mostrarTarjetaIndividual(data, tipo) {
        // Seleccionamos el contenedor de la tarjeta individual
        const contenedorResultado = document.getElementById('buscador-vino-id');
    
        // Limpiamos cualquier contenido previo
        contenedorResultado.innerHTML = '';
    
        // Creamos un contenedor para la tarjeta
        const tarjeta = document.createElement('div');
        tarjeta.classList.add('col-md-4', 'tarjeta-individual'); // Añadir clases de Bootstrap y el estilo personalizado
    
        // Dependiendo del tipo, mostramos los datos relevantes
        if (tipo === 'vinos') {
            // Vino: nombre, bodega, cepas, y partidas
            tarjeta.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${data.nombre}</h5>
                        <p class="card-text">Bodega: ${data.bodega}</p>
                        <p class="card-text">Cepa(s): ${data.cepas.join(', ')}</p>
                        <p class="card-text">Partidas: ${data.partidas.join(', ')}</p>
                    </div>
                </div>
            `;
        } else if (tipo === 'bodegas' || tipo === 'cepas') {
            // Bodega o Cepa: solo nombre
            tarjeta.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${data.nombre}</h5>
                    </div>as
                </div>
            `;
        }
    
        // Añadimos la tarjeta al contenedor de resultados
        contenedorResultado.appendChild(tarjeta);
    
        // Aseguramos que el contenedor sea visible
        contenedorResultado.classList.remove('d-none');
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
