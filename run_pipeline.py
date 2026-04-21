import os

print("🚀 Starting data pipeline...\n")

# Run scraper
print("🔄 Running scraper...")
os.system("python scraper/scraper.py")

# Run cleaning
print("🧹 Cleaning data...")
os.system("python processing/clean_data.py")

# Store in database
print("💾 Storing in database...")
os.system("python database/db.py")

print("\n✅ Pipeline executed successfully!")