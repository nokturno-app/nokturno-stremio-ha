# Nokturno pro Stremio

Doplněk pro Stremio a Nuvio, který běží doma v Home Assistantu. Přihlašovací údaje ke zdrojům tak
neprocházejí přes žádný cizí server.

## Jak začít
1. Spusť doplněk a otevři **Otevřít webové rozhraní** (nebo `http://<IP Home Assistantu>:7140/configure`
   z telefonu či počítače ve stejné síti).
2. Vyplň vlastní úložiště a případně účty zdrojů, u každého dej **Ověřit**.
3. **Přidat do Stremia** nebo **Přidat do Nuvia**.

Stremio chce doplněk z jiného zařízení přes HTTPS. Formulář otevřený přes IP adresu proto dá do doplňku adresu
`https://<IP s pomlčkami>.my.local-ip.co:7141` sám. Nuvio si vystačí s `http://<IP>:7140`.
Home Assistantu nastav v routeru pevnou IP (rezervace DHCP), jinak doplněk po změně adresy přestane fungovat.

## Volby
| Volba | Význam |
|---|---|
| `host` | adresa poslechu, `0.0.0.0` = celá síť, za reverzní proxy `127.0.0.1` |
| `soukroma` | soukromá instance: doplněk obslouží jen nastavení povolená tlačítkem *Povolit na tomhle serveru* na `/configure` |
| `port` | HTTP: nastavení na `/configure` a doplněk pro Nuvio (výchozí 7140) |
| `https_port` | HTTPS přes local-ip.co pro Stremio v síti (výchozí 7141) |
| `enable_https` | vypnutím zůstane jen HTTP |
| `tmdb_key` | nepovinný vlastní klíč TMDB pro katalogy TMDB |
| `stats` | anonymní statistiky používání |
| `crash_reports` | hlášení o pádech doplňku |
| `update_url` | nech prázdné |

## Aktualizace
Doplněk si nové verze stahuje sám: při startu a pak každých 6 hodin. Novou verzi ověří a když nenaběhne,
vrátí předchozí. Nová verze doplňku v Home Assistantu vychází jen při změně kontejneru.

Nápověda: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-aplikace
