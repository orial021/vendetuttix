<script>
    let resp = ""
    let nombre = "";
    function handle(e){
        
        const target = e.target;
        nombre = e.target.value;
        EmptyForm()
    };
    function EmptyForm(){
        if (nombre.length === 0){
            resp = "No me has dicho como te llamas"
        }
        else {
            resp = `${nombre} valido.
            Bienvenida ${nombre}`
        }
    }
       

        
</script>

<input type="text" placeholder="nombre"
 class="texto" on:keyup={handle}/>

<p>{resp}</p>

<input type="text" placeholder="usuario" class="texto"/>
<input type="text" placeholder="password" class="texto"/>
<input type="text" placeholder="email" class="texto"/>
<input type="text" placeholder="rol" class="texto"/>




<button> limpiar</button>


<button on:click={EmptyForm}>
    enviar mensaje
</button>
<style>
    .texto {
        font-size: 2.5rem;

        }
    p {
        font-size: 1.8rem;

    }
    button {
        font-size: 1.5rem;
    }
</style>