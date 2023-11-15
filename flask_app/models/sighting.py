from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Sasquatch:
    db = "exam_schema"

    def __init__(self, data):
        self.sighting_table_id = data.get('sighting_table_id')
        self.user_id = data.get('user_id')
        self.location = data.get('location')
        self.number_of_sasquatches = data.get('number_of_sasquatches')
        self.what_happened = data.get('what_happened')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.date_of_sighting = data.get('date_of_sighting') 
        self.reported_by = None

    @staticmethod
    def validate_sasquatch_data(data):
        errors = []

        if not (data.get('location') and data.get('number_of_sasquatches') and data.get('what_happened') and data.get('date_of_sighting')):
            errors.append("Please fill in all fields")

        if len(data.get('what_happened', '')) < 50:
            errors.append("Please provide a detailed description (at least 50 characters) of what happened")

        if not str(data.get('number_of_sasquatches', '')).isdigit() or int(data.get('number_of_sasquatches', 0)) < 1:
            errors.append("Number of Sasquatches must be at least 1")

        return errors

    @classmethod
    def get_user_sasquatch_sightings(cls, user_id):
        query = """
            SELECT * FROM sightings
            WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, {'user_id': user_id})

        return [cls(result) for result in results] if results else []

    @classmethod
    def get_sasquatch_by_id(cls, sasquatch_id):
        query = """
            SELECT * FROM sightings
            WHERE sighting_table_id = %(sasquatch_id)s
            LIMIT 1;
        """
        result = connectToMySQL(cls.db).query_db(query, {'sasquatch_id': sasquatch_id})

        return cls(result[0]) if result else None

    @classmethod
    def create_sasquatch_sighting(cls, data):
        query = """
            INSERT INTO sightings (user_id, location, number_of_sasquatches, what_happened, date_of_sighting)
            VALUES (%(user_id)s, %(location)s, %(number_of_sasquatches)s, %(what_happened)s, %(date_of_sighting)s);
        """
        result = connectToMySQL(cls.db).query_db(query, data)

        if result:
            return result
        else:
            return None

    @classmethod
    def update_sasquatch_sighting(cls, sasquatch_id, data):
        query = """
            UPDATE sightings
            SET location = %(location)s, number_of_sasquatches = %(number_of_sasquatches)s,
                what_happened = %(what_happened)s, date_of_sighting = %(date_of_sighting)s
            WHERE sighting_table_id = %(sasquatch_id)s;
        """
        data['sasquatch_id'] = sasquatch_id
        connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_sasquatch_sighting(cls, sasquatch_id):
        query = """
            DELETE FROM sightings
            WHERE sighting_table_id = %(sasquatch_id)s;
        """
        connectToMySQL(cls.db).query_db(query, {'sasquatch_id': sasquatch_id})

    @classmethod
    def get_all_sasquatch_sightings(cls):
        query = """
            SELECT *
            FROM sightings
            JOIN users ON sightings.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        
        if results:
            all_sasquatch_sightings = []

            for result in results:
                one_result = cls(result)

                one_sasquatch_user_data = {
                    'id': result['id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'email': result['email'],
                    'password': result['password'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at']
                }
                reported_by_user = user.User(one_sasquatch_user_data)
                one_result.reported_by = reported_by_user
                all_sasquatch_sightings.append(one_result)

            return all_sasquatch_sightings
        else:
            return []