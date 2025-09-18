class Movie():
    def __init__(self, title, genre, year, movie_id):
        self.title = title
        self.genre = genre
        self.year = year
        self.movie_id = movie_id
        self.is_available = True

    def rent_movie(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_movie(self):
        if self.is_available == False:
            self.is_available = True
            return True
        return False

    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"{self.title} {self.genre} {self.year} {self.movie_id} - {availability}"

class Customer():
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_movies = []

    def list_rented_movies(self):
        if not self.rented_movies:
            print("No movies found")
        else:
            for movies in self.rented_movies:
                print(movies)

    def __str__(self):
        return f"{self.name} {self.customer_id}"
    
class RentalStore():
    def __init__(self):
        self.movie_inventory = []
        self.customers = []

    def add_movie(self, movie):
        self.movie_inventory.append(movie)

    def remove_movie(self, movie_id):
        for new_movie in self.movie_inventory:
            if new_movie.movie_id == movie_id:
                if new_movie.is_available:
                    self.movie_inventory.remove(new_movie)
                    print(f"{new_movie.title} removed successfully")
                    return True
                else:
                    print(f"{new_movie.title} has been borrowed")
                    return False
        print(f"{movie_id} not found")        
        return False


    def register_customer(self, customer):
        for new_customer in self.customers:
            if new_customer.customer_id == customer.customer_id:
                print(f"{customer} is already registered")
                return False

        self.customers.append(customer)
        print(f"{customer} registered successfully!")
        return True
        
        

    def rent_movie(self, customer_id, movie_id):
        for movie in self.movie_inventory:
            if movie.movie_id == movie_id:
                if movie.is_available:
                    for customer in self.customers:
                        if customer.customer_id == customer_id:
                            movie.is_available = False
                            print(f"You've borrowed {movie.title} successfully")
                            customer.rent_movie.append(movie)
                            return True
                    return "You're not a registered member"
                    return False
                
            print(f"{movie.title} is not available")
            
        print(f"{movie_id} not found")
        return False

    def return_movie(self, customer_id, movie_id):
        for movie in self.movie_inventory:
            if movie.movie_id == movie_id:
                if not movie.is_available:
                    for customer in self.customers:
                        if customer.customer_id == customer_id:
                            movie.is_available = True
                            print(f"You've returned {movie.title} successfully")
                            customer.rent_movie.remove(movie)
                            return True
                    return "You're not a registered member"
                    return False
                
            print(f"{movie.title} is already in the library")
        print(f"{movie_id} not found")
        return False

    def list_movie(self):
        if not self.movie_inventory:
            print("No movies found")
        else:
            for movies in self.movie_inventory:
                print(movies)

    def search(self, query):
        query = query.lower()
        results = []
        
        for movie in self.movie_inventory:
            if (query in movie.title.lower() or 
                query in movie.genre.lower() or 
                query in movie.movie_id or
                query in movie.year):
                results.append(movie)

        if results:
            print(f"Found {len(results)} movie(s):")
            for movie in results:
                print(movie)
        else:
            print(f"No movies found matching '{query}'")
        
        return results

m1 = Movie("Inception", "Science Fiction", "2010", "M001")
m2 = Movie("The Dark Knight", "Action", "2008", "M002")
m3 = Movie("Black Panther", "Superhero", "2018", "M003")

c1 = Customer("Alice Johnson", "C001")
c2 = Customer("Bob Smith", "C002")
c3 = Customer("Charlie Brown", "C003")

rent = RentalStore()

rent.movie_inventory = [m1,m2,m3]
rent.remove_movie("M002")
rent.register_customer(c1)
rent.search("2018")