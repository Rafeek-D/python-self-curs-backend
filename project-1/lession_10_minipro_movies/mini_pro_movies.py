from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
def get_root():
    



# here is the src="{movie.Poster}" get the Poster from the response of the
def movie_card_func (movie):
    return '''  <a
        href="#"
        target="_blank"
        class="movie-card"
      >
        <img
          src="{movie.Poster}"
          alt="Pi Poster"
        />
        <div class="movie-info">
          <h2>Pi</h2>
          <p>Year: 2008</p>
          <p>⭐ Rating: 9.0</p>
        </div>
      </a> '''