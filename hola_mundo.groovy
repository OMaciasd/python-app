import java.text.SimpleDateFormat
import java.util.Date

def date = new Date()
def formattedDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(date)

println 'Hola, Mundo!'
println "La fecha actual es: ${formattedDate}"
