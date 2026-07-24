import React, { useState, useEffect } from 'react';

/* ==================================================================================
   PAGE LÉGALE — Mentions légales · Confidentialité · CGU · CGV
   Accessible sur skipro-app.com/legal (voir main.jsx).
   Les champs [À COMPLÉTER] sont à remplir avant toute commercialisation.
   Ces documents sont des modèles standards : une validation par un professionnel
   du droit reste recommandée avant publication définitive.
   ================================================================================== */

const C = {
  snow: '#F4F7FA', card: '#FFFFFF', iceLine: '#E3EAF1',
  navy: '#0F2C46', ink: '#22313F', inkSoft: '#5A6B7A', glacier: '#2F7FB8'
};

const EDITEUR = {
  nom: '[À COMPLÉTER — nom / raison sociale]',
  statut: '[À COMPLÉTER — ex : micro-entreprise, SASU…]',
  siret: '[À COMPLÉTER — n° SIRET]',
  adresse: '[À COMPLÉTER — adresse professionnelle]',
  email: 'contact@skipro-app.com',
  tva: '[À COMPLÉTER — n° TVA intracommunautaire, ou « TVA non applicable, art. 293 B du CGI »]'
};

const DERNIERE_MAJ = '25 juillet 2026';

function H2({ children }) {
  return <h2 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 17, fontWeight: 700, color: C.navy, margin: '28px 0 10px' }}>{children}</h2>;
}
function P({ children }) {
  return <p style={{ fontSize: 14, lineHeight: 1.7, color: C.ink, marginBottom: 10 }}>{children}</p>;
}
function Li({ children }) {
  return <li style={{ fontSize: 14, lineHeight: 1.7, color: C.ink, marginBottom: 4 }}>{children}</li>;
}

function MentionsLegales() {
  return (
    <>
      <H2>Éditeur du site</H2>
      <P>Le site skipro-app.com (ci-après « SkiPro » ou « le Service ») est édité par : {EDITEUR.nom}, {EDITEUR.statut}, immatriculé(e) sous le numéro SIRET {EDITEUR.siret}, dont l'adresse professionnelle est {EDITEUR.adresse}.</P>
      <P>Contact : {EDITEUR.email}</P>
      <P>Directeur de la publication : {EDITEUR.nom}</P>
      <P>TVA : {EDITEUR.tva}</P>
      <H2>Hébergement</H2>
      <P>Le site est hébergé par Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis (vercel.com).</P>
      <P>Les données applicatives sont hébergées par Supabase, Inc. (supabase.com), sur des serveurs situés dans l'Union européenne.</P>
      <H2>Propriété intellectuelle</H2>
      <P>L'ensemble des éléments du site (structure, textes, logos, interface) est la propriété exclusive de l'éditeur, sauf mention contraire. Toute reproduction sans autorisation préalable est interdite.</P>
      <H2>Signalement</H2>
      <P>Pour signaler un contenu ou un problème : {EDITEUR.email}</P>
    </>
  );
}

function Confidentialite() {
  return (
    <>
      <P><em>Dernière mise à jour : {DERNIERE_MAJ}</em></P>
      <H2>1. Qui traite vos données ?</H2>
      <P>Le responsable du traitement des données liées aux comptes moniteurs est {EDITEUR.nom} ({EDITEUR.email}).</P>
      <P>Cas particulier des données clients saisies via un lien de réservation public : le moniteur concerné est responsable du traitement des données de ses propres clients ; SkiPro agit en tant que sous-traitant au sens de l'article 28 du RGPD (hébergement et mise à disposition de l'outil).</P>
      <H2>2. Données collectées</H2>
      <ul style={{ paddingLeft: 22, marginBottom: 10 }}>
        <Li><strong>Moniteurs (titulaires de compte)</strong> : adresse email, paramètres professionnels (nom, tarifs, horaires, coordonnées bancaires de facturation saisies volontairement), données d'abonnement (via Stripe).</Li>
        <Li><strong>Clients des moniteurs (formulaire public)</strong> : nom, prénom, téléphone, email, nationalité, langue, âge, niveau, station, préférence de mode de paiement, message libre.</Li>
      </ul>
      <P>Aucune donnée de carte bancaire n'est traitée ni stockée par SkiPro : les paiements d'abonnement sont traités directement par Stripe.</P>
      <H2>3. Finalités et bases légales</H2>
      <ul style={{ paddingLeft: 22, marginBottom: 10 }}>
        <Li>Fourniture du service de gestion de réservations — exécution du contrat.</Li>
        <Li>Facturation de l'abonnement — exécution du contrat et obligations légales.</Li>
        <Li>Notifications par email (nouvelles réservations) — intérêt légitime / exécution du contrat.</Li>
      </ul>
      <P>Aucune donnée n'est vendue ni utilisée à des fins publicitaires.</P>
      <H2>4. Sous-traitants</H2>
      <ul style={{ paddingLeft: 22, marginBottom: 10 }}>
        <Li>Supabase, Inc. — hébergement de la base de données et authentification (serveurs UE).</Li>
        <Li>Vercel Inc. — hébergement du site et des fonctions serveur.</Li>
        <Li>Stripe, Inc. — traitement des paiements d'abonnement.</Li>
        <Li>Resend (Plus Five Five, Inc.) — envoi des emails de notification.</Li>
      </ul>
      <H2>5. Durées de conservation</H2>
      <P>Les données de compte sont conservées tant que le compte est actif, puis supprimées dans un délai de 12 mois après clôture. Les données de facturation sont conservées 10 ans conformément aux obligations comptables. Les données de réservation sont conservées par le moniteur tant qu'il en a l'usage ; il peut les supprimer à tout moment depuis l'application.</P>
      <H2>6. Vos droits</H2>
      <P>Conformément au RGPD, vous disposez de droits d'accès, de rectification, d'effacement, de limitation, de portabilité et d'opposition. Pour les exercer : {EDITEUR.email}. Pour les données saisies via le lien public d'un moniteur, adressez-vous en priorité à ce moniteur. Vous pouvez introduire une réclamation auprès de la CNIL (cnil.fr).</P>
      <H2>7. Cookies</H2>
      <P>SkiPro utilise uniquement des traceurs techniques strictement nécessaires (session d'authentification). Aucun cookie publicitaire ou de mesure d'audience tierce n'est déposé.</P>
    </>
  );
}

function CGU() {
  return (
    <>
      <P><em>Dernière mise à jour : {DERNIERE_MAJ}</em></P>
      <H2>1. Objet</H2>
      <P>Les présentes Conditions Générales d'Utilisation encadrent l'accès et l'utilisation de SkiPro, outil de gestion de réservations destiné aux moniteurs de sports de glisse indépendants, ainsi que l'utilisation du formulaire de réservation public par leurs clients.</P>
      <H2>2. Compte</H2>
      <P>La création d'un compte nécessite une adresse email valide. Le titulaire est responsable de la confidentialité de ses identifiants et des activités réalisées depuis son compte.</P>
      <H2>3. Utilisation du service</H2>
      <P>L'utilisateur s'engage à fournir des informations exactes, à respecter la réglementation applicable à son activité professionnelle, et à ne pas détourner le service de sa finalité (spam, contenu illicite, tentative d'intrusion…).</P>
      <H2>4. Rôle de SkiPro</H2>
      <P>SkiPro est un outil de gestion mis à disposition des moniteurs. SkiPro n'est pas partie aux contrats conclus entre un moniteur et ses clients : les cours, leurs prix, leur exécution et leur encaissement relèvent de la seule responsabilité du moniteur. Les préférences de paiement indiquées dans le formulaire public sont purement informatives ; aucun paiement de cours n'est traité par SkiPro.</P>
      <H2>5. Disponibilité</H2>
      <P>SkiPro s'efforce d'assurer une disponibilité maximale du service, sans garantie d'absence d'interruption. Des maintenances peuvent être réalisées ; les interruptions ne donnent pas droit à indemnisation, hors dispositions des CGV relatives à l'abonnement.</P>
      <H2>6. Données</H2>
      <P>Le traitement des données personnelles est décrit dans la Politique de confidentialité. Le moniteur s'engage à respecter le RGPD vis-à-vis des données de ses clients qu'il gère via le service.</P>
      <H2>7. Propriété intellectuelle</H2>
      <P>Le service, son interface et son code demeurent la propriété de l'éditeur. L'abonnement confère un droit d'utilisation personnel, non exclusif et non cessible.</P>
      <H2>8. Résiliation</H2>
      <P>L'utilisateur peut cesser d'utiliser le service et demander la suppression de son compte à tout moment. L'éditeur peut suspendre un compte en cas de manquement grave aux présentes CGU, après notification.</P>
      <H2>9. Droit applicable</H2>
      <P>Les présentes CGU sont soumises au droit français. En cas de litige, une solution amiable sera recherchée avant toute action judiciaire.</P>
    </>
  );
}

function CGV() {
  return (
    <>
      <P><em>Dernière mise à jour : {DERNIERE_MAJ}</em></P>
      <H2>1. Objet</H2>
      <P>Les présentes Conditions Générales de Vente régissent la souscription de l'abonnement payant SkiPro par des professionnels (moniteurs indépendants), auprès de {EDITEUR.nom} ({EDITEUR.siret}).</P>
      <H2>2. Offre et prix</H2>
      <P>L'abonnement SkiPro est proposé au tarif de 29 € par mois {EDITEUR.tva.startsWith('[') ? '[À COMPLÉTER — préciser TTC ou HT selon le régime de TVA]' : ''}. Le prix en vigueur est celui affiché au moment de la souscription. Toute évolution tarifaire sera notifiée au moins 30 jours avant son application et ne s'appliquera qu'aux périodes suivantes.</P>
      <H2>3. Paiement</H2>
      <P>Le paiement s'effectue mensuellement par carte bancaire via Stripe. L'abonnement est reconduit tacitement chaque mois. En cas d'échec de paiement, l'accès aux fonctionnalités payantes peut être suspendu après notification.</P>
      <H2>4. Durée et résiliation</H2>
      <P>L'abonnement est sans engagement : il peut être résilié à tout moment depuis l'application (Paramètres). La résiliation prend effet à la fin de la période mensuelle en cours, qui reste due. Aucun remboursement au prorata n'est effectué pour une période entamée.</P>
      <H2>5. Droit de rétractation</H2>
      <P>Le service étant destiné à des professionnels dans le cadre de leur activité, le droit de rétractation prévu pour les consommateurs n'est pas applicable, conformément à l'article L221-3 du Code de la consommation, sauf exceptions légales.</P>
      <H2>6. Garanties et responsabilité</H2>
      <P>SkiPro est fourni « en l'état ». La responsabilité de l'éditeur, tous préjudices confondus, est limitée au montant des sommes effectivement versées par l'abonné au cours des 12 derniers mois. L'éditeur ne saurait être tenu responsable des pertes de revenus liées aux relations entre le moniteur et ses clients.</P>
      <H2>7. Facturation</H2>
      <P>Les justificatifs de paiement sont accessibles via l'espace de facturation Stripe. Pour toute demande de facture : {EDITEUR.email}.</P>
      <H2>8. Droit applicable et litiges</H2>
      <P>Les présentes CGV sont soumises au droit français. À défaut d'accord amiable, les tribunaux compétents seront ceux du ressort du siège de l'éditeur.</P>
    </>
  );
}

const TABS = [
  { id: 'mentions', label: 'Mentions légales', Comp: MentionsLegales },
  { id: 'confidentialite', label: 'Confidentialité', Comp: Confidentialite },
  { id: 'cgu', label: 'CGU', Comp: CGU },
  { id: 'cgv', label: 'CGV', Comp: CGV }
];

export default function LegalPage({ initialTab }) {
  const [tab, setTab] = useState(TABS.some(t => t.id === initialTab) ? initialTab : 'mentions');
  useEffect(() => {
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600;700&display=swap';
    link.rel = 'stylesheet'; document.head.appendChild(link);
  }, []);
  const Active = TABS.find(t => t.id === tab).Comp;
  return (
    <div style={{ minHeight: '100vh', background: C.snow, fontFamily: 'Inter, sans-serif', padding: '32px 16px 60px' }}>
      <div style={{ maxWidth: 720, margin: '0 auto' }}>
        <a href="/" style={{ display: 'inline-flex', alignItems: 'center', gap: 9, fontFamily: "'Space Grotesk', sans-serif", fontWeight: 700, fontSize: 19, color: C.navy, textDecoration: 'none', marginBottom: 20 }}>
          <span style={{ width: 20, height: 20, borderRadius: 5, background: 'linear-gradient(135deg, #2E7D5B 33%, #2F7FB8 33% 66%, #000 66%)' }} />
          SkiPro
        </a>
        <h1 style={{ fontFamily: "'Space Grotesk', sans-serif", fontSize: 26, fontWeight: 700, color: C.navy, marginBottom: 18 }}>Informations légales</h1>
        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', marginBottom: 22 }}>
          {TABS.map(t => (
            <button key={t.id} onClick={() => setTab(t.id)} style={{
              padding: '8px 14px', borderRadius: 9, cursor: 'pointer', fontSize: 13.5, fontWeight: 600,
              border: `1px solid ${tab === t.id ? C.glacier : C.iceLine}`,
              background: tab === t.id ? C.glacier + '18' : C.card,
              color: tab === t.id ? C.glacier : C.ink
            }}>{t.label}</button>
          ))}
        </div>
        <div style={{ background: C.card, border: `1px solid ${C.iceLine}`, borderRadius: 16, padding: '10px 28px 28px' }}>
          <Active />
        </div>
      </div>
    </div>
  );
}
