# Tweets Collector

This is a simple python script to search tweets and to save them into a text file.

To run this script download this repository and follow these steps:

## Setings

1. In the `twitter-settings.json` file fill in your twitter `consumer_key`, `consumer_secret`, `access_key` and `access_secret`
2. In the `search-query-parameters.json` file fill in the search parameters

❗️ Query parameter `keywords` take all the keywords you want to search. Inside the string separate them with space.

❗️ Query parameter `from_user` can be with or without `@` prefix.

❗️ Query parameters `language`, `from_user`, `since` and `until` can be empty.

❗️ Query parameters `since` and `until` must be in `yyyy-mm-dd` format and you can not search tweets older than 7 days.

## Run script

### macOS

### Windows

### Linux

## Schritt-für-Schritt-Anleitung
1. Entpacken Sie die ZIP-Datei!
2. Erstellen Sie einen neuen Ordner mit dem Namen `collected-tweets` in dem entpackten Ordner.
3. Füllen Sie `consumer_key`, `consumer_secret`, `access_key` und `access_secret` in der `twitter-settings.json`-Datei aus.
4. Füllen Sie die Suchparameter in der `search-query-parameters.json`-Datei aus.
5. **Folgende Suchparameter können bestimmt werden:**
    - `keywords` – Führen Sie hier alle Stichwörter, nach denen Sie suchen möchten, trennen Sie die einzelnen Stichwörter je mit einem Leerzeichen.
    - `from_user` – Füllen Sie hier @Handle aus, und zwar mit/ohne @.
    - `language` – Füllen Sie hier die beliebte Sprache aus – in unserem Fall: de – es wird dann bei jedem Tweet überprüft, ob es sich tatsächlich um einen deutschen Text handelt.
    - `since` und `until` müssen immer folgend formatiert werden: `jjjj-mm-tt`. Es kann in der Standard-API-Version nur innerhalb von sieben Tagen gesucht werden – die gesuchten Tweets können also nicht älter als sieben Tage sein!

Suchparameter `language`, `from_user`, `since` und `until` können auch leer bleiben.
