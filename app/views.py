from flask import render_template
from app import app, db
from .models import stats, games, venues, teams
from sqlalchemy.sql import func

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html',title='Home')

@app.route('/grounds')
def grounds():
    ground = venues.query.order_by(venues.venue_name)
    return render_template('grounds.html', venues = ground)

# OLD GROUNDS QUERY
#@app.route('/grounds_charts/<query_type>')
#def grounds_charts(query_type):
#    chart_query = db.session.query(func.avg(getattr(stats, query_type)).label("total"), venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id)).filter(getattr(stats, query_type) > 0).group_by(venues.venue_name)
#    return render_template('grounds_charts.html', chart_query = chart_query)

@app.route('/grounds_charts/<query_type>/<min_year>/<max_year>')
def grounds_charts(query_type,min_year,max_year):
    min_year = min_year + '-01-01'
    max_year = max_year + '-12-12'
    chart_query = db.session.query(func.avg(getattr(stats, query_type)).label("total"), venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id)).filter(getattr(stats, query_type) > 0).filter(games.date >= min_year).filter(games.date <= max_year).group_by(venues.venue_name)
    return render_template('grounds_charts.html', chart_query = chart_query)

@app.route('/teams_charts/<query_type>')
def teams_charts(query_type):
    chart_query = db.session.query(func.avg(getattr(stats, query_type)).label("total"), teams.team_name).join(teams).filter((teams.team_id == stats.team_id)).filter(getattr(stats, query_type) > 0).group_by(teams.team_name)
    return render_template('teams_charts.html', chart_query = chart_query)

@app.route('/year_charts/<query_type>')
def year_charts(query_type):
    chart_query = db.session.query(func.avg(getattr(stats, query_type)).label("total"), func.strftime('%Y', games.date).label("Year")).join(games).filter(stats.game_id == games.game_id).group_by("Year")
    #select AVG(stats.tackles), teams.team_name, strftime('%Y', games.date) as Year from stats, games, teams where stats.game_id = games.game_id AND stats.team_id = teams.team_id GROUP BY teams.team_name,Year
    return render_template('year_charts.html', chart_query = chart_query)

@app.route('/teams/<query_type>')
def teams_dash(query_type):
    chart_query = db.session.query(func.avg(getattr(stats, query_type)).label("total"), teams.team_name, games.date).join(teams, games.game_id==stats.game_id).filter((teams.team_id == stats.team_id)).group_by(teams.team_name)
    return render_template('teams.html', chart_query = chart_query)

@app.route('/grounds_kicks')
def grounds_kicks():
    #gkicks = stats.query.get(stats.kicks, venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id))
    #gkicks = stats.query.order_by(stats.game_id, stats.kicks)
    #ggame = games.query.order_by(games.game_id)
    #gkicks = stats.query.all()
    #gkicks = db.session.query(stats.kicks, venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id))
    gkicks = db.session.query(func.avg(stats.kicks).label("total_kicks"), venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id)).group_by(venues)

    return render_template('grounds_kicks.html', gkicks = gkicks)

@app.route('/grounds_handballs')
def grounds_handballs():
    #ghandballs = stats.query.get(stats.handballs, venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id))
    #ghandballs = stats.query.order_by(stats.game_id, stats.handballs)
    #ggame = games.query.order_by(games.game_id)
    #ghandballs = stats.query.all()
    #ghandballs = db.session.query(stats.handballs, venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id))
    ghandballs = db.session.query(func.avg(stats.handballs).label("total_handballs"), venues.venue_name).join(games, venues).filter((games.game_id == stats.game_id)).group_by(venues)

    return render_template('grounds_handballs.html', ghandballs = ghandballs)
