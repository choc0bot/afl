from app import db

class teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(64), index=True, unique=True)

#class Venues(db.Model):
#    venue_id = db.Column(db.Integer, primary_key=True)
#    venue_name = db.Column(db.String(128), index=True, unique=True)

class venues(db.Model):
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(128), index=True, unique=True)

class games(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    round = db.Column(db.String(128))
    home_team_id = db.Column(db.Integer,  db.ForeignKey('teams.team_id'))
    away_team_id = db.Column(db.Integer,  db.ForeignKey('teams.team_id'))
    venue_id = db.Column(db.Integer,  db.ForeignKey('venues.venue_id'))
    attendance = db.Column(db.Integer)
    away_team = db.relationship('teams', primaryjoin='games.away_team_id == teams.team_id')
    home_team = db.relationship('teams', primaryjoin='games.home_team_id == teams.team_id')
    venue = db.relationship('venues', primaryjoin='games.venue_id == venues.venue_id')

class stats(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), primary_key=True)
    kicks = db.Column(db.Integer)
    handballs = db.Column(db.Integer)
    disposals = db.Column(db.Integer)
    marks = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    hitouts = db.Column(db.Integer)
    frees_for = db.Column(db.Integer)
    frees_against = db.Column(db.Integer)
    goals_kicked = db.Column(db.Integer)
    behinds_kicked = db.Column(db.Integer)
    behinds_rushed = db.Column(db.Integer)
    scoring_shots = db.Column(db.Integer)
    inside_50s = db.Column(db.Integer)
    in50s_score = db.Column(db.Integer)
    in50s_goal = db.Column(db.Integer)
    game = db.relationship('games')
    team = db.relationship('teams')