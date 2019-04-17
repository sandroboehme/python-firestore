import os
from google.cloud import firestore

if __name__ == '__main__':
    current_folder = os.path.dirname(os.path.abspath(__file__))
    abs_auth_path = os.path.join(current_folder, 'auth.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = abs_auth_path
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada2',
        u'last': u'Lovelace',
        u'born': 1815
    })

    # Then query for documents
    users_ref = db.collection(u'users')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
