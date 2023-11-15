from flask import render_template, redirect, request, session, url_for, flash
from flask_app import app
from flask_app.models.sighting import Sasquatch
from flask_app.models.user import User
from datetime import datetime

@app.route('/sasquatch_sightings/new', methods=['GET'])
def new_sasquatch_sighting():
    return render_template('add_sasquatch_sighting.html')

@app.route('/create/sasquatch_sighting', methods=['POST'])
def create_sasquatch_sighting():

    current_date = datetime.now().strftime('%Y-%m-%d')

    if 'user_id' in session:  
        user_id = session['user_id']
        
        location = request.form['location']
        number_of_sasquatches = request.form['number_of_sasquatches']
        what_happened = request.form['what_happened']
        date_of_sighting = request.form['date_of_sighting']

        sasquatch_data = {
            'user_id': user_id,
            'location': location,
            'number_of_sasquatches': number_of_sasquatches,
            'what_happened': what_happened,
            'date_of_sighting': date_of_sighting
        }

        errors = Sasquatch.validate_sasquatch_data(sasquatch_data)

        if errors:
            for error in errors:
                flash(error, "error")
            return redirect(url_for('new_sasquatch_sighting'))

        # If validation passes, create the Sasquatch sighting
        Sasquatch.create_sasquatch_sighting(sasquatch_data)
        flash("Successfully added Sasquatch sighting", "success")
        return redirect(url_for('homepage', current_date=current_date))
    else:
        flash("You must log in to access that", "login")
        return redirect('/')

@app.route('/sasquatch_sightings/view/<int:sasquatch_id>')
def view_sasquatch_sighting(sasquatch_id):
    sasquatch_data = Sasquatch.get_sasquatch_by_id(sasquatch_id)

    if not sasquatch_data:
        flash("Sasquatch sighting not found", "error")
        return redirect(url_for('homepage'))

    return render_template('view_sasquatch_sighting.html', sasquatch=sasquatch_data)

# edit Sasquatch sighting
@app.route('/sasquatch_sightings/edit/<int:sasquatch_id>', methods=['GET', 'POST'])
def edit_sasquatch_sighting(sasquatch_id):
    sasquatch_data = Sasquatch.get_sasquatch_by_id(sasquatch_id)

    # Check if the Sasquatch sighting exists
    if not sasquatch_data:
        flash("Sasquatch sighting not found", "error")
        return redirect(url_for('homepage'))

    current_date = datetime.now().strftime('%Y-%m-%d')

    # Check if the current user is the owner of the Sasquatch sighting
    if 'user_id' in session and session['user_id'] == sasquatch_data.user_id:
        if request.method == 'POST':

            location = request.form['location']
            number_of_sasquatches = request.form['number_of_sasquatches']
            what_happened = request.form['what_happened']
            date_of_sighting = request.form['date_of_sighting']


            updated_data = {
                'location': location,
                'number_of_sasquatches': number_of_sasquatches,
                'what_happened': what_happened,
                'date_of_sighting': date_of_sighting
            }

            errors = Sasquatch.validate_sasquatch_data(updated_data)

            if errors:
                for error in errors:
                    flash(error, "error")
                return render_template('edit_sasquatch_sighting.html', sasquatch=sasquatch_data, current_date=current_date)

            # If validation passes, update the Sasquatch sighting
            Sasquatch.update_sasquatch_sighting(sasquatch_data.sighting_table_id, updated_data)
            flash("Sasquatch sighting updated successfully", "success")
            return redirect(url_for('homepage'))

        return render_template('edit_sasquatch_sighting.html', sasquatch=sasquatch_data, current_date=current_date)
    else:
        flash("You thought I didn't protect against that?", "hacker")
        return redirect('/')

# delete sighting
@app.route('/sightings/delete/<int:sasquatch_id>')
def delete_sighting(sasquatch_id):
    # Retrieve the recipe by ID from the database
    sasquatch_data = Sasquatch.get_sasquatch_by_id(sasquatch_id)

    # Check if the recipe exists
    if not sasquatch_data:
        flash("Sighting not found", "error")
        return redirect(url_for('homepage'))

    # Check if the current user is the owner of the recipe
    if session['user_id'] == sasquatch_data.user_id:
        # Delete the recipe from the database
        Sasquatch.delete_sasquatch_sighting(sasquatch_data.sighting_table_id)
        flash("Sighting deleted successfully", "success")
        return redirect(url_for('homepage'))
    else:
        flash("You thought I didn't protect against that?", "hacker")
        return redirect('/')