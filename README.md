# holo-lingo-backend
Build the image:
docker build -t hololingo-back .

Create the container:
docker run -p 8000:8000 --name hololingo-back  hololingo-back