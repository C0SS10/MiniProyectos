/* Te pasan un array con la duración de cada entrega. El formato de la duración es HH:mm:ss, las entregas empiezan a las 00:00:00 y el límite de tiempo es 07:00:00.
La función debe devolver el tiempo que les faltará o el tiempo que les sobrará para terminar las entregas. El formato de la duración devuelta debe ser HH:mm:ss.
Si terminan antes de las 07:00:00, el tiempo restante hasta las 07:00:00 debe ser mostrado con un signo negativo. Por ejemplo, si sobran 1 hora y 30 minutos, devuelve -01:30:00 */

function calculateTime(deliveries: string[]): string {
  const totalSeconds = deliveries.reduce((acc, hour) => {
    const [hours, minutes, seconds] = hour.split(':').map(Number);
    return acc + hours * 3600 + minutes * 60 + seconds;
  }, 0);

  let remainingSeconds = 7 * 3600 - totalSeconds;
  const sign = remainingSeconds <= 0 ? '' : '-';
  remainingSeconds = Math.abs(remainingSeconds);
  const remainingHours = Math.floor(remainingSeconds / 3600).toString().padStart(2, '0');
  const remainingMinutes = Math.floor((remainingSeconds % 3600) / 60).toString().padStart(2, '0');
  const remainingSecondsLeft = (remainingSeconds % 60).toString().padStart(2, '0');

  return `${sign}${remainingHours}:${remainingMinutes}:${remainingSecondsLeft}`;
}