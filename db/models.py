import os
import asyncio
import re
# from sqlalchemy import text
from dotenv import load_dotenv
# from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

DATABASE_URL='postgresql://neondb_owner:npg_RyXYMBvFN7f1@ep-lingering-shape-a8cqnx6v-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'

async def create_table_and_insert():
    async_url = re.sub(r"^postgresql:", "postgresql+asyncpg:", DATABASE_URL)
    engine = create_async_engine(async_url, echo=True)

    async with engine.begin() as conn:
        # Create table if not exists
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS vehicle_identification (
                id SERIAL PRIMARY KEY,
                registration_number VARCHAR(20),
                chassis_number VARCHAR(30),
                engine_number VARCHAR(30),
                make VARCHAR(50),
                model VARCHAR(50),
                body_type VARCHAR(30),
                color VARCHAR(30),
                year_of_manufacture INT,
                country_of_origin VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """))

        # Insert sample record
        await conn.execute(text("""
            INSERT INTO vehicle_identification
            (registration_number, chassis_number, engine_number, make, model, body_type, color, year_of_manufacture, country_of_origin)
            VALUES ('KDA 123A', 'JHMCM56557C404453', 'ENG123456789', 'Toyota', 'Corolla', 'Saloon', 'White', 2018, 'Japan');
        """))

    await engine.dispose()

asyncio.run(create_table_and_insert())
