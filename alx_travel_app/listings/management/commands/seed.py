import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import time


class Command(BaseCommand):
    """
    Usage examples:
    Seed 50,000 listings using the default batch size of 10,000:
        python manage.py seed --number 50000

    Seed 100,000 listings using a smaller batch size of 5,000:
        python manage.py seed --number 100000 --batch-size 5000

    Seed 1,000,000 listings with a larger batch size of 20,000:
        python manage.py seed --number 1000000 --batch-size 20000
    """
    help = "Seeds the database with a large number of sample listings using batch processing."

    def add_arguments(self, parser):
        DEFAULT_LISTING_COUNT = 50000
        parser.add_argument(
            "--number",
            type=int,
            help="The total number of listings to create.",
            default=DEFAULT_LISTING_COUNT,
        )
        DEFAULT_BATCH_SIZE = 10000
        parser.add_argument(
            "--batch-size",
            type=int,
            help="The number of listings to create in each batch.",
            default=DEFAULT_BATCH_SIZE,
        )

    def handle(self, *args, **options):
        number = options["number"]
        batch_size = options["batch_size"]

        self.stdout.write(
            f"Seeding {number} listings using a batch size of {batch_size}..."
        )
        start_time = time.time()

        # Initialize the Faker generator
        fake = Faker('en_US')

        self.stdout.write("Clearing old listing data...")
        Listing.objects.all().delete()

        # Get or create a sample user to own the listings
        user, created = User.objects.get_or_create(
            username="defaultuser",
            defaults={"password": "password", "email": "user@example.com"},
        )
        if created:
            self.stdout.write("Created default user 'defaultuser'.")
        else:
            self.stdout.write("Using existing default user 'defaultuser'.")

        batch = []
        total_created = 0

        for i in range(1, number + 1):
            listing = Listing(
                title=fake.catch_phrase(),
                description=fake.text(max_nb_chars=500),
                price_per_night=round(random.uniform(50.00, 500.00), 2),
                address=fake.address(),
                num_bedrooms=random.randint(1, 6),
                num_bathrooms=random.randint(1, 4),
                max_guests=random.randint(1, 12),
                owner=user,
            )
            batch.append(listing)

            if len(batch) == batch_size:
                Listing.objects.bulk_create(batch)
                total_created += len(batch)
                self.stdout.write(f"Inserted batch! Total created: {total_created} / {number}")
                batch = []

        # Insert any remaining listings that didn't fill a full batch
        if batch:
            Listing.objects.bulk_create(batch)
            total_created += len(batch)
            self.stdout.write(
                f"Inserted the final batch! Total created: {total_created} / {number}"
            )

        end_time = time.time()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded the database with {total_created} listings in {end_time - start_time:.2f} seconds."
            )
        )


