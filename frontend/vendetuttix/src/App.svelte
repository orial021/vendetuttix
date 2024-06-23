<script>
    let elements = [
        "Comprar papas",
        "limpiar",
        "correo",
        "llamar Lucia"
    ]
</script>

{#each elements as e, num}
<div>
    <strong>
        Tarea {num + 1}:
    </strong>
    <span>{e}</span>
</div>
{/each}

<style>
    strong {
        font-size: 3rem;
        
    }
    span {
        font-size: 3rem;
    }
</style>